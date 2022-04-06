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

YES_ANSWERS = ["yes", "y", "ok", "sure", "yeah"]
NO_ANSWERS = ["no", "n", "nah"]
EXIT_WORDS = ["bye", "exit"]


def get_name():
    name_str = input("What is your name? ")
    print("Elmo: Hello {0}".format(name_str))

# def display_question(question):
#     """
#     Iterate over key/value pairs in dict and print them
#     """
#     for key, value in question_dict.items():
#         if key == question:
#             print(value)


while True:
    #q3 = input("Elmo: The {activity} takes place every {day} at {hour}. ")
    # input("Elmo: Excellent! Elmo did it all by himself")
    q1 = input("Would you like to sign up for the activities? ")
    q1_str = q1.lower()
    print(q1)
    if q1_str in YES_ANSWERS:
        q2 = input("Which activity would you like to sign up for? ")
        q2_str = q2.lower()
        print(q2)
    elif q1.lower() in NO_ANSWERS:
        q_joke = input("Elmo: Would you like to hear a joke? ")
        print(q_joke)
        print("Elmo: joke")
    else:
        q_conf = input("Elmo: I am not sure what you mean... Can you use other words? ")
        if q_conf == "yes".lower():
            print(q2)
        elif q_conf == "no".lower():
            print(q_joke)
        else:
            print(input("Elmo: What do you mean?"))

    bye = input("Elmo: Are you leaving? ")

    if bye == "yes".lower():
        print("Elmo: Take care <3")
    else:
        play = input("Do you want to start over?")


# def update_worksheet(data, worksheet):
#     """
#     Receives a name of the User to be inserted into a worksheet
#     Update the relevant worksheet with the data provided
#     """
#     print(f"Updating {worksheet} worksheet...\n")
#     worksheet_to_update = SHEET.worksheet(worksheet)
#     worksheet_to_update.append_row(data)
#     print(f"{worksheet} worksheet updated successfully\n")


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
