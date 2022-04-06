import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('elmo_act')

activities = SHEET.worksheet('activities')
data = activities.get_all_values()

print(data)


while True:
    """
    Start of the new session,
    Get name provided by the User via input
    Run a while loop to collect a valid string of data from the user
    via the terminal. The loop will repeatedly request data, until it is valid.
    """
    print("Hi my name is Elmo and I will help you register for the activities.")
    name_str = input("What is your name? ")

    print("Elmo: Hello {0}".format(name_str))
    q1 = input("Elmo: Would you like to sign up for the activities? ")

    if q1 == "yes".lower():
        print("Huray")
    elif q1 == "no".lower():
        print("oh noooo")
    else:
        q_conf = input("Elmo: I am not sure what you mean... Can you use other words? ")
        if q_conf == "yes".lower():
            print("Huray")
        elif q_conf == "no".lower():
            print("oh noooo")
        else:
            print(input("Seems like I am missing some words here."))

    bye = input("Elmo: Are you leaving? ")

    if bye == "yes".lower():
        print("Elmo: Take care <3")
    else:
        play = input("Do you want to start over?")