import gspread
from google.oauth2.service_account import Credentials
import sys

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('elmo_act')

# activities = SHEET.worksheet('activities')
# data = activities.get_all_values()
# print(data)

YES_ANSWERS = ["yes", "y", "ok", "sure", "yeah"]
NO_ANSWERS = ["no", "n", "nah"]
EXIT_WORDS = ["bye", "exit"]
JOKE_ANS = ["joke"]

def get_name():
    name_str = input("Elmo: What is your name?\nYou: ")
    print("Elmo: Hello {0}".format(name_str))

# def display_question(question):
#     """
#     Iterate over key/value pairs in dict and print them
#     """
#     for key, value in question_dict.items():
#         if key == question:
#             print(value)

def get_activities():
    """
    Collects first row of data from activities worksheet,
    and returns the data as a list of strings.
    """
    activ = SHEET.worksheet("activities").get_all_values()
    activ_row = activ[0]
    activ_string = ''
    for x in activ_row:
        activ_string += ' ' + x

    return activ_string

activities = get_activities()

def display_date():
    """
    Collects first row of data from activities worksheet,
    and returns the data as a list of strings.
    """
    dates = SHEET.worksheet("activities").get_all_values()
    date_act = dates[0]
    date = dates[-1]

    print(date)    

display_date()

def choose_activ():
    print("Elmo: The activities are:" + get_activities())
    inp2 = input("Elmo: Which activity would you like to sign up for?\nYou: ")
    inp2_str = inp2.lower()
    if inp2_str not in activities:
        print("Elmo: I do not have {0} on my list!".format(inp2))
        print("Elmo: Try again.")
        choose_activ()
    else:
        print("Elmo: The {0} classes take place every Friday at 16:00.".format(inp2))

def tell_joke():
    joke = input("Elmo: Would you like to hear funny joke?\nYou: ")
    if joke in YES_ANSWERS or joke in JOKE_ANS:
        print("joke")
        tell_joke()
    else:
        say_bye()

def confirm():
    confirmation = input("Elmo: Is that OK for you?\nYou: ")
    if confirmation not in YES_ANSWERS:
        print("Elmo: Do you want to start again?")
        restart()
    else:
        print("Elmo: Hurray! You are now on the list!")
        tell_joke()

def say_bye():      
    bye = input("Elmo: Are you leaving now?\nYou: ")
    bye_str = bye.lower()
    if bye_str in YES_ANSWERS:
        print("Elmo: Take care <3")
        sys.exit()
    else:
        restart()

def restart():
    restart = str(input("Elmo: Would you like to start again?\nYou: "))
    if restart in YES_ANSWERS:
        restart = ('Y')
    elif restart in NO_ANSWERS:
        say_bye()
    else:
        tell_joke()

def start():
    while restart not in NO_ANSWERS:
        inp1 = input("Elmo: Would you like to sign up for the activities?\nYou: ")
        inp1_str = inp1.lower()
        if inp1_str in YES_ANSWERS:
            choose_activ()
            confirm()
        elif inp1_str in NO_ANSWERS:
            tell_joke()
        else:
            say_bye()

def main():
#     """
#     Run all program functions
#     """
    get_name()
    start()

print(main())