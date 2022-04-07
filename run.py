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
JOKE = ["joke"]

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

q1 = "Elmo: Would you like to sign up for the activities?\nYou: "
q2 = "Elmo: Which activity would you like to sign up for?\nYou: "
q3 = "Elmo: Is that OK for you?\nYou: "
q4 = "Elmo: Do you want to sign up for another classes?\nYou: "
q5 = "Elmo: I am not sure what you mean... Can you use other words?"
q6 = "Elmo: Would you like to hear funny joke?\nYou: "
q7 = "Elmo: Did you like it?\nYou: "
q8 = "Elmo: Would you like more jokes?\nYou: "
q9 = "Elmo: Is there anything else I can do for you?\nYou: "


while True:
    get_name()
    inp1 = input(q1)
    inp1_str = inp1.lower()
    if inp1_str in YES_ANSWERS:
        print("Elmo: The activities are: " + get_activities())
        inp2 = input(q2)
        inp2_str = inp2.lower()
        if inp2_str in activities:
            print("Elmo: The {0} classes take place every Friday at 16:00.".format(inp2))
            inp3 = input(q3)
            inp3_str = inp3.lower()
            if inp3_str in YES_ANSWERS:
                # add name to the list
                print("Elmo: Excellent! You are on the list!")
                inp4 = input(q4)
                inp4_str = inp4.lower()
                if inp4 in YES_ANSWERS:
                    print(inp2)
                elif inp4 in NO_ANSWERS:
                    inp6 = input(q6)
                    inp6_str = inp6.lower()
                    if inp6_str in YES_ANSWERS or inp6_str in JOKE:
                        print("Elmo: joke")
                        inp7 = input(q7)
                        inp7_str = inp7.lower()
                        if inp7_str in YES_ANSWERS:
                            print("Elmo: joke")
                            print(inp7)
                        elif inp7_str in NO_ANSWERS:
                            print("Elmo: It was fun!")
                            inp9 = input(q9)
                            inp9_str = inp9.lower()
                            if inp9 in YES_ANSWERS:
                                print(inp1_str)
                            elif inp9_str in NO_ANSWERS:
                                print("bye bye")
                        else:
                            inp5 = input(q5)
                            inp5_str = inp5.lower()
                            if inp5_str in YES_ANSWERS:
                                print(inp1) 
                            else:
                                print("bye")
                    else:
                        print("Elmo: Oh no! I thought it will make you laugh.")
                        inp9 = input(inp9)
                else:
                    print(inp5)
            elif inp3_str in NO_ANSWERS:
                print(inp4)
            else:
                print(inp5)
        else:
            print(inp5)
    elif inp1_str in NO_ANSWERS:
        print(inp6)
    else:
        print(inp5)


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