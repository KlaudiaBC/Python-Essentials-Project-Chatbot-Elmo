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

# activities = SHEET.worksheet('activities')
# data = activities.get_all_values()
# print(data)

YES_ANSWERS = ["yes", "y", "ok", "sure", "yeah"]
NO_ANSWERS = ["no", "n", "nah"]
EXIT_WORDS = ["bye", "exit"]


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
        activ_string += ' ' + x + ','

    return activ_string

activities = get_activities()

while True:
    get_name()
    q1 = input("Elmo: Would you like to sign up for the activities?\nYou: ")
    q1_str = q1.lower()
    if q1_str in YES_ANSWERS:
        print("Elmo: The activities are: " + get_activities())
        q2 = input("Elmo: Which activity would you like to sign up for?\nYou: ")
        q2_str = q2.lower()
        if q2_str in activities:
            print("Elmo: The {0} classes take place at every Friday at 16:00.".format(q2))
            q3 = input("Elmo: Is that OK for you?\nYou: ")
            q3_str = q3.lower()
            if q3_str in YES_ANSWERS:
                print("Elmo: Excellent! You are on the list!")
                print(input("Elmo: Do you want to sign up for another classes?\nYou: "))
            else:
                print("OK.")
        else:
            print("I got lost")
    elif q1_str in NO_ANSWERS:
        q_joke = input("Elmo: Would you like to hear a joke?\nYou: ")
        print(q_joke)
        print("Elmo: joke")
    else:
        q_conf = input("Elmo: I am not sure what you mean... Can you use other words?\nYou: ")
        if q_conf == "yes".lower():
            print(q2)
        elif q_conf == "no".lower():
            print(q_joke)
        else:
            print(input("Elmo: What do you mean?\nYou: "))

    bye = input("Elmo: Are you leaving?\nYou: ")

    if bye == "yes".lower():
        print("Elmo: Take care <3")
    else:
        play = input("Do you want to start over?")


# def main():
#     """
#     Run all program functions
#     """
#     data = get_name()
#     name_data = name_str
#     update_worksheet(name_data, "students")

print("Hi! My name is Elmo! :)")
print("I can help you register for the activities of your choice.")
print("I can also tell you a funny joke!")




print(get_name())