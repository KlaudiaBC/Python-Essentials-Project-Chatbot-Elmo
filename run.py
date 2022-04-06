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


def get_name_data():
    """
    Start of the new session,
    Get name provided by the User via input
    Run a while loop to collect a valid string of data from the user
    via the terminal. The loop will repeatedly request data, until it is valid.
    """
    while True:
        print("Hi my name is Elmo and I will help you register for the activities.")

        name_str = input("What is your name?: \n")

        if validate_data(name_str):
            print("Hello {0}".format(name_str))
            break

    return name_str


def validate_data(value):
    """
    Inside the try, converts all string values into integers.
    Raises ValueError if strings cannot be converted into int,
    or if there aren't exactly 6 values.
    """
    try:
        if value == None:
            raise ValueError(
                f"Never heard of that name. Can you use the letters?"
            )
    except ValueError as e:
        print(f"Invalid data: {e}, please try again.\n")
        return False

    return True

print(get_name_data())