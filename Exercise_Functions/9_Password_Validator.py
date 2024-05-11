''' Variant 9.1
def validate_password(password):
    is_valid = True
    if len(password) not in range(6, 11):
        print("Password must be between 6 and 10 characters")
        is_valid = False
    if not password.isalnum():
        print("Password must consist only of letters and digits")
        is_valid = False
    counter_of_digits = 0
    for character in password:
        if character.isdigit():
            counter_of_digits += 1
    if counter_of_digits < 2:
        print("Password must have at least 2 digits")
        is_valid = False
    return is_valid

some_password = input()
password_is_valid = validate_password(some_password)
if password_is_valid:
    print("Password is valid")
'''

''' Variant 9.2 '''
def length_validation(password):
    if len(password) not in range(6, 11):
        print("Password must be between 6 and 10 characters")
        return False
    return True


def symbol_validation(password):
    if not password.isalnum():
        print("Password must consist only of letters and digits")
        return False
    return True


def two_digits_validation(password):
    counter_of_digits = 0
    for character in password:
        if character.isdigit():
            counter_of_digits += 1
    if counter_of_digits < 2:
        print("Password must have at least 2 digits")
        return False
    return True

some_password = input()
password_is_valid = [length_validation(some_password), symbol_validation(some_password), two_digits_validation(some_password)]
if all(password_is_valid):
    print("Password is valid")