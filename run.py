"""Add required libraries"""
import sys
import json
import random
import gspread
from google.oauth2.service_account import Credentials
import spacy
from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()
nlp = spacy.load('en_core_web_sm')

# Connect and add creds into an external worksheet
SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('elmo_act')

# Declare required variables
YES_ANSWERS = ["yes", "y", "ok", "ye", "sure", "yeah"]
NO_ANSWERS = ["no", "n", "nah"]
EXIT_WORDS = ["exit", "bye", "go"]
FUNNY_ANSWERS = ["hahaha", "funny", "lol", "lmao", "hehe", "hihi", "silly"]
tags = []
patterns = []
responses = []
activity = SHEET.worksheet("activities").get_all_values()


# Functions connected with sign up process:
def get_date(activities, dates):
    """
    Collects first row of data from activities worksheet,
    and returns the data as a list of strings.
    """
    for index, value in enumerate(activities):
        print(f"- {value} - {dates[index]}")


def input_text(input_message):
    """
    Asking user for input untill he
    provide a valid response,
    imput must be greater than 0
    """
    while True:
        input_value = input(input_message)
        if len(input_value) > 0:
            break
    return input_value


def choose_activity(player_name, activities, dates):
    """
    Display the time of chosen activities
    and request a confirmation from the user
    Once the User provide the required data,
    push this data into a spreadsheet
    """
    print("Elmo: The activities are as follow:")
    get_date(activities, dates)
    print("Elmo: Which activity would you like to sign up for?")
    inp = input_text("You: ")
    inp_str = inp.lower()
    if inp_str in EXIT_WORDS:
        say_bye(player_name)
    elif inp_str not in activities:
        print(f"Elmo: I do not have {inp} on my list :(")
    else:
        print(f"Elmo: I will add you to the list for the {inp_str} classes.")
        confirmation = input_text("Elmo: Is that correct?\nYou: ")
        if confirmation in YES_ANSWERS:
            student = [player_name, inp_str]
            save_name(student, 'students')
        elif confirmation in NO_ANSWERS:
            restart(player_name)
        else:
            process_answer(player_name, inp_str)


def say_bye(player_name):
    """
    Defining conversation end protocol
    If User request to end the program,
    exit the terminal, else: restart or process the answer
    """
    bye = input_text("Elmo: Are you leaving now?\nYou: ")
    bye_str = bye.lower()
    if bye_str in YES_ANSWERS:
        print(f"Elmo: Bye bye {player_name}! Take care! <3")
        sys.exit()
    elif bye_str in NO_ANSWERS:
        restart(player_name)
    else:
        process_answer(player_name, bye_str)


def show_themes():
    """
    Display random hint for a User
    acording to the conversation flow
    """
    sentenses = [
        "Elmo: Please, be free to ask me anything about the school.",
        "Elmo: Do you feel happy or sad? I am here to listen.",
        "Elmo: Type: contact to find a person, who you can talk to.",
        "Elmo: You can ask me about the prices or about the address.",
        "Elmo: Type 'joke' and let me cheer you up! :)"
    ]

    print(random.choice(sentenses))


def restart(player_name):
    """
    If user request to restart,
    render a question with help offer
    The answer will define: random reponse,
    or option to exit the terminal
    """
    print("Elmo: Is there anything else I can help you with?")
    show_themes()
    restart_question = str(input_text("You: "))
    restart_str = restart_question.lower()
    if restart_str in YES_ANSWERS:
        print("Elmo: What would you like to know?")
        lead_question = str(input_text("You: "))
        process_answer(player_name, lead_question)
    elif restart_str in [*NO_ANSWERS, *EXIT_WORDS]:
        say_bye(player_name)
    else:
        process_answer(player_name, restart_str)


def start(player_name, activities, dates):
    """
    Defining conversation start protocol
    Render a first main question,
    answer will then define the direction
    of the conversation flow
    """
    while restart not in NO_ANSWERS:
        print("Elmo: Would you like to sign up for the activities?")
        inp1 = input_text("You: ")
        inp1_str = inp1.lower()
        if inp1_str in YES_ANSWERS:
            choose_activity(player_name, activities, dates)
        elif inp1_str in NO_ANSWERS:
            restart(player_name)
        else:
            if inp1_str in EXIT_WORDS:
                say_bye(player_name)
            else:
                process_answer(player_name, inp1_str)


def save_name(data, worksheet):
    """
    Export the desired data into an external worksheet
    """
    students = SHEET.worksheet(worksheet)
    students.append_row(data)
    print("Elmo: Excellent! You are now on the list!")
    restart(player_name=data[0])


# Functions connected with chatbot converation
def process_answer(player_name, message):
    """
    Tokenize and lemmatize the words
    from the input, then search for it
    in the patterns and via tag can
    relate to correct, random answer
    """
    if "who" in message:
        print("Elmo: I am Elmo, a chatbot who likes to joke.")

    for msg in message:
        msg = nlp(message)
        for token in msg:
            msg_lem = token.lemma_
    for pattern in patterns:
        if msg_lem in pattern[0]:
            for response in responses:
                if pattern[1] == response[1]:
                    res = random.choice(response[0])
                    print("Elmo:", res)
                    user_answer = input_text("You: ")
                    process_answer(player_name, user_answer)
                    if pattern[1] == "joke":
                        if user_answer in FUNNY_ANSWERS:
                            print("Elmo: Haha, that was funny, wasn't it? :)")
                    elif pattern[1] in EXIT_WORDS:
                        say_bye(player_name)
                    else:
                        restart(player_name)


# Adding integration and calling the main function


def welcome():
    """
    Initiate the program
    Display greeting and instructions
    """
    line_a = "   =======================================================\
===============   \n"
    print("")
    print(line_a)
    print("                                   WELCOME!\n")
    print("                     CHATBOT ELMO IS READY TO REGISTER YOU")
    print("                      FOR THE ACTIVITIES OF YOUR CHOICE.")
    print("                        HE IS CHEEKY AND LIKES TO JOKE")
    print("                      SO DON'T LET HIM GET CARRIED AWAY :)")
    print("                        YOU CAN TELL HIM HOW YOU FEEL")
    print("                   OR ASK FOR INFORMATION ABOUT OUR SCHOOL:")
    print("                        HE KNOWS THE ADDRESS, CONTACT")
    print("                      AND ALL ABOUT AVAILABLE ACTIVITIES.\n")
    print("                         PUNCTUATION MAY CONFUSE ELMO")
    print("                     AS HE IS ONLY NOW STARTING TO LEARN.")
    print("                   TO END THE CONVERSATION JUST TYPE: EXIT")
    print("                          I HOPE YOU'LL HAVE FUN! :)\n")
    print(line_a)


def main():
    """
    Starts the application:
    Import all the data
    Display welcome message
    """
    data_file = open('intents.json', encoding='UTF-8').read()
    intents = json.loads(data_file)

    for intent in intents['Intents']:
        if intent['patterns'] not in patterns:
            patterns.append((intent['patterns'], intent['tag']))
        if intent['responses'] not in responses:
            responses.append((intent['responses'], intent['tag']))

    welcome()
    print("Elmo: Hi. I am Elmo, your virtual friend :)")
    name_str = input_text("Elmo: What is your name?\nYou: ")
    print(f"Elmo: Hello {name_str}! Nice to meet you!")
    start(name_str, activities=activity[0], dates=activity[1])


main()
