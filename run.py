# Add required libraries
import gspread
from google.oauth2.service_account import Credentials
import sys

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
YES_ANSWERS = ["yes", "y", "ok", "sure", "yeah"]
NO_ANSWERS = ["no", "n", "nah"]
EXIT_WORDS = ["bye", "exit"]
JOKE_ANS = ["joke"]


# def display_question(question):
#     """
#     Iterate over key/value pairs in dict and print them
#     """
#     for key, value in question_dict.items():
#         if key == question:
#             print(value)

==================================================

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
        print("Elmo: I do not have {0} on my list!".format(inp))
        print("Elmo: Try again.")
        choose_activ()
    else:
        print("Elmo: The {0} classes take place every Friday at 16:00.".format(inp))
        confirmation = input("Elmo: Is that OK for you?\nYou: ")
        if confirmation not in YES_ANSWERS:
            print("Elmo: Do you want to start again?")
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
        print("Elmo: Take care {0} <3".format(name_str))
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
        elif inp1_str in NO_ANSWERS:
            tell_joke()
        else:
            say_bye()

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

name_str = input("Elmo: What is your name?\nYou: ")
print(name_str)
print("Elmo: Hello {0}".format(name_str))