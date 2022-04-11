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
EXIT_WORDS = ["bye", "exit"]


# Functions connected with sign up process

def get_activities():
    """
    Collects first row of data from activities worksheet,
    and returns the data as a list of items.
    """
    activ = SHEET.worksheet("activities").get_all_values()
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
    pass

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
        print(f"Elmo: The {inp} classes take place every Friday at 16:00.")
        confirmation = input("Elmo: Is that OK for you?\nYou: ")
        if confirmation in YES_ANSWERS:
            student = [name_str, inp_str]
            save_name(student, 'students')
        elif confirmation in NO_ANSWERS:
            restart()
        else:
            process_answer(inp_str)

def tell_joke():
    """
    Render random joke from the "jokes" list
    After the user confirmed, he wants to hear a joke
    or requested it via placing in the input word "joke"
    """
    joke = input("Elmo: Would you like to hear funny joke?\nYou: ")
    if joke in YES_ANSWERS:
        print("joke")
    elif joke in NO_ANSWERS:
        say_bye()
    else:
        process_answer(joke)

def say_bye():
    """
    If User request to end the program,
    exits the terminal,
    else: offer to display a joke
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
    If user request to restart, render a first question
    from the sign in process (function: start)
    else: offer to dispaly a joke 
    """
    restart_q = str(input("Elmo: Is there anything I can help you with?\nYou: "))
    if restart_q in YES_ANSWERS:
        lead_q = str(input("Elmo: What would you like to know?\nYou: "))
        process_answer(lead_q)
    elif restart_q in NO_ANSWERS:
        say_bye()
    else:
        process_answer(restart_q)


def start():
    """
    Render a first main question, which will then
    define the direction of the conversation:
    sign up process or small talk/jokes 
    """
    while restart not in NO_ANSWERS:
        inp1 = input("Elmo: Would you like to sign up for the activities?\nYou: ")
        inp1_str = inp1.lower()
        if inp1_str in YES_ANSWERS:
            choose_activ()
        elif inp1_str in NO_ANSWERS:
            say_bye()
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
tags = []
patterns = []
responses = []
ignore_words = ['?', '!']

data_file = open('intents.json').read()
# Convert the JSON data into Python object
intents = json.loads(data_file)

# assign the data from json file
# into a lists with connected tags
for intent in intents['Intents']:
    if intent['patterns'] not in patterns:
        patterns.append((intent['patterns'], intent['tag']))
    if intent['responses'] not in responses:
        responses.append((intent['responses'], intent['tag']))


def process_answer(message):
    for msg in message:
        # Lemmatization -  create base word,
        # in attempt to represent related words,
        # tokenized words are converted into shorten
        # root words to remove redundancy
        msg = nlp(message)
        for token in msg:
            msg_lem = token.lemma_

    # Loops through a patterns and
    # search for the one which contains
    # word from the input, return tag
    for pattern in patterns:
        if msg_lem in pattern[0]:
            # Loops through the responses to match the tag
            # with a tag from patterns and render
            # a random response from the list
            for response in responses:
                if pattern[1] == response[1]:
                    res = random.choice(response[0])
            print(res)
            restart()                   


#Defining conversation start/end protocols
def main():
    """
    Initiate the program
    Call functions in the specified order
    """
    start()
    message = input()
    process_answer(message)

name_str = input("Elmo: What is your name?\nYou: ")
print(f"Elmo: Hello {name_str}!")
start()