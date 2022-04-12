# Add required libraries
import gspread
from google.oauth2.service_account import Credentials
import sys
import nltk
from nltk.stem import WordNetLemmatizer
nltk.download('punkt')
nltk.download('wordnet')
nltk.download('omw-1.4')
import json
import numpy as np
import random
lemmatizer = WordNetLemmatizer()
import spacy
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
STOP_WORDS = ["?", "!", "you", "the", "a", "an", "so", "what"]
tags = []
patterns = []
responses = []
activ = SHEET.worksheet("activities").get_all_values()

# Functions connected with sign up process:

def get_activities():
    """
    Collects first row of data from activities worksheet,
    and returns the data as a list of items.
    """
    activ_row = activ[0]
    activ_string = ''
    for x in activ_row:
        activ_string += ' ' + x + ','
    return activ_string

activities = get_activities()

def get_date():
    """
    Collects first row of data from activities worksheet,
    and returns the data as a list of strings.
    """
    activ_ = activ[0]
    date = activ[1]


def choose_activ():
    """
    Display the time of chosen activities
    and request a confirmation from the user
    Once the User provide the required data,
    push this data into a spreadsheet
    """
    print("Elmo: The activities are:" + get_activities())
    inp = input("Elmo: Which activity would you like to sign up for?\nYou: ")
    inp_str = inp.lower()
    if inp_str not in activities:
        print(f"Elmo: I do not have {inp} on my list!")
        choose_activ()
    else:
        print(f"Elmo: I will add you to the list for the {inp_str} classes.")
        confirmation = input("Elmo: Is that correct?\nYou: ")
        if confirmation in YES_ANSWERS:
            student = [name_str, inp_str]
            save_name(student, 'students')
        elif confirmation in NO_ANSWERS:
            restart()
        else:
            process_answer(inp_str)

def say_bye():
    """
    Defining conversation end protocol
    If User request to end the program,
    exit the terminal, else: restart or process the answer
    """ 
    bye = input("Elmo: Are you leaving now?\nYou: ")
    bye_str = bye.lower()
    if bye_str in YES_ANSWERS:
        print(f"Elmo: Bye bye {name_str}! Take care! <3")
        sys.exit()
    elif bye_str in NO_ANSWERS:
        restart()    
    else:
        process_answer(bye_str)

def restart():
    """
    If user request to restart,
    render a question with help offer
    The answer will define: random reponse,
    or option to exit the terminal
    """
    restart_q = str(input("Elmo: Is there anything else I can help you with?\nYou: "))
    if restart_q in YES_ANSWERS:
        lead_q = str(input("Elmo: What would you like to know?\nYou: "))
        process_answer(lead_q)
    elif restart_q in NO_ANSWERS:
        say_bye()
    else:
        process_answer(restart_q)

def start():
    """
    Defining conversation start protocol
    Render a first main question,
    answer will then define the direction
    of the conversation flow
    """
    while restart not in NO_ANSWERS:
        inp1 = input("Elmo: Would you like to sign up for the activities?\nYou: ")
        inp1_str = inp1.lower()
        if inp1_str in YES_ANSWERS:
            choose_activ()
        elif inp1_str in NO_ANSWERS:
            restart()
        else:
            process_answer(inp1_str)

def save_name(data, worksheet):
    """
    Export the desired data into an external worksheet
    """
    students = SHEET.worksheet(worksheet)
    students.append_row(data)
    print("Elmo: Excellent! You are now on the list!")
    restart()


# Functions connected with chatbot converations

# Initialize Chatbot Training
data_file = open('intents.json').read()
"""Convert the JSON data into Python object"""
intents = json.loads(data_file)

for intent in intents['Intents']:
    """Assign the data from json file to variables"""
    if intent['patterns'] not in patterns:
        patterns.append((intent['patterns'], intent['tag']))
    if intent['responses'] not in responses:
        responses.append((intent['responses'], intent['tag']))

def process_answer(message):
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
                    if pattern[1] == "joke":
                        print("Elmo: I hope I made you laugh :)")
                    elif pattern[1] == "exit":
                        say_bye()     
                    else:
                        restart()


# Adding integration and calling the main function

def welcome():
    """
    Initiate the program
    Display greeting and instructions
    """
    print("")
    print("WELCOME!\n")
    print("CHATBOT ELMO IS READY TO REGISTER YOU FOR THE ACTIVITIES OF YOUR CHOICE.")
    print("HE IS CHEEKY AND LIKES TO JOKE.")
    print("DON'T LET HIM CARRY AWAY WITH HIS TASKS :)")
    print("YOU CAN TELL HIM HOW YOU FEEL OR ASK FOR INFORMATION ABOUT OUR SCHOOL:")
    print("HE KNOWS THE ADDRESS, CONTACT AND ALL ABOUT AVAILABLE ACTIVITIES.\n")
    print("TOO LONG SENTENCES MAY CONFUSE ELMO")
    print("AS HE IS VERY SMALL AND ONLY NOW STARTING TO LEARN.")
    print("HAVE FUN! :)\n")

welcome()
print("Elmo: Hi. I am Elmo, your virtual friend.")
name_str = input("Elmo: What is your name?\nYou: ")
print(f"Elmo: Hello {name_str}! Nice to meet you!")
start()