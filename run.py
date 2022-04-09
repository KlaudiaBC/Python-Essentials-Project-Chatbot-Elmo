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
JOKE_ANS = ["joke"]


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
        print("Elmo: Try again.")
        choose_activ()
    else:
        print(f"Elmo: The {inp} classes take place every Friday at 16:00.")
        confirmation = input("Elmo: Is that OK for you?\nYou: ")
        if confirmation not in YES_ANSWERS:
            restart()
        else:
            student = [name_str, inp_str]
            save_name(student, 'students')
            tell_joke()

def tell_joke():
    """
    Render random joke from the "jokes" list
    After the user confirmed, he wants to hear a joke
    or requested it via placing in the input word "joke"
    """
    joke = input("Elmo: Would you like to hear funny joke?\nYou: ")
    if joke in YES_ANSWERS or joke in JOKE_ANS:
        print("joke")
        tell_joke()
    else:
        say_bye()

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
    else:
        restart()

def restart():
    """
    If user request to restart, render a first question
    from the sign in process (function: start)
    else: offer to dispaly a joke 
    """
    restart = str(input("Elmo: Would you like to start again?\nYou: "))
    if restart in YES_ANSWERS:
        restart = ('Y')
    elif restart in NO_ANSWERS:
        say_bye()
    else:
        tell_joke()

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
        else:
            tell_joke()

def save_name(data, worksheet):
    """
    Export the desired data into an external worksheet
    """
    students = SHEET.worksheet(worksheet)
    students.append_row(data)
    print("Elmo: Excellent! You are now on the list!")


def main():
    """
    Initiate the program
    Call functions in the specified order
    """
    start()

# name_str = input("Elmo: What is your name?\nYou: ")
# print(f"Elmo: Hello {name_str}!")
# start()

# Functions connected with chatbot converations
# Initialize Chatbot Training
words = []
classes = []
documents = []
responses = []
ignore_words = ['?', '!']

data_file = open('intents.json').read()
# Convert the JSON data into Python object
intents = json.loads(data_file)


# Text preprocessing
for intent in intents['Intents']:
    for pattern in intent['patterns']:
        # take each word and tokenize it
        w = nltk.word_tokenize(pattern)
        words.extend(w)
        # adding documents (patterns)
        documents.append((w, intent['tag']))
        # adding classes (tags) to the class list
        if intent['tag'] not in classes:
            classes.append(intent['tag'])

# Lemmatization -  create base word,
# in attempt to represent related words,
# tokenized words are converted into shorten
# root words to remove redundancy

# Create bag of word:
bag = [lemmatizer.lemmatize(w) for w in words if w not in ignore_words]
bag = sorted(list(set(words)))

# Create a sorted list of items:
classes = sorted(list(set(classes)))

print(len(documents), "documents", documents)
# print(len(classes), "classes", classes)
# print(len(words), "unique lemmatized words", words)

# taking each response from each intent and connect it with a tag,
# building a list of responses
for intent in intents['Intents']:
    for response in intent['responses']:
        # adding documents (patterns)
        responses.extend((response, intent['tag']))

print(responses)


message = input()

def process_answer():
    for msg in message:
        # take each word and lemma
        msg = nlp(message)
        for token in msg:
            msg_list = token.lemma_

    print(msg_list)

    check = any(item in msg_list for item in bag)
    if check == True:
        print("Answer")
    else:
        print("No ans")

process_answer()



# def display_question(question):
#     """
#     Iterate over key/value pairs in dict and print them
#     """
#     for key, value in question_dict.items():
#         if key == question:
#             print(value)