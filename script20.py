class PasswordTooShortError(Exception):
    pass

def validate_password(password):
    try:
        if len(password) < 6:
            raise PasswordTooShortError("Password must be at least 6 characters long.")
    except ValueError:
        return "Invalid Password!"

def enter_password():
    password = input("Please enter your password.")
    return password


s = enter_password()
validate_password(s)
