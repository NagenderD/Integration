# Custom exception class
class InvalidInputError(Exception):
    pass

def get_user_age():
    try:
        age = int(input("Please enter your age: "))
        if age < 0 or age > 150:
            raise InvalidInputError("Age should be between 0 and 150.")
        else:
            print("Valid age entered:", age)
    except ValueError:
        print("Invalid input. Please enter a valid age as a number.")
    except InvalidInputError as e:
        print(e)

# Getting user's age and handling exceptions
get_user_age()
