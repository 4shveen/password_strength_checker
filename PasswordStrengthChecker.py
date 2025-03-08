'''Python Assignment: Password Strength Checker with Feedback Loop
Implement a password strength checker that evaluates a given password while reinforcing the
understanding of fundamental data types like int, float, bool, string, and list. The program shou
provide real-time feedback and allow users to retry until they create a strong password.'''

category = "" # category initialised as empty string

password_history = [] # storage for passwords already used and also to append accepted new strong passwords.

while category != "Strong":
    # Take input from user (string handling)
    password = input("Enter password: ")

    # Check password strength using different data types
        # 1. upper, lower, number, special characters checks. Note that we define a list of special characters here to avoid unexpected characters and unicode symbols.
    is_lower = any (c.islower() for c in password)
    is_upper = any (c.isupper() for c in password)
    is_digit = any (c.isdigit() for c in password)
    is_special = any (c in "!@#$%^&*()-_=+[]{};:'\",.<>?/\\|`~" for c in password)

        # 2. password length, character types included
    password_length = len(password)
    letter_count = sum (c.isalpha() for c in password)
    number_count = sum (c.isdigit() for c in password)
    special_character_count = sum (c in "!@#$%^&*()-_=+[]{};:'\",.<>?/\\|`~" for c in password)

        # 3. -Store sets of character categories (letters, numbers, special characters).
            #-Maintain a history of previously entered passwords.
    if password in password_history:
        print ("Passwords cannot be recycled. Please try a new one.")
        continue

    # Password categorisation and feedback
    if password_length < 6:
        category = "Weak"
        print ("Weak password. Try using numbers and special characters.")
    elif special_character_count == 0:
        category = "Medium"
        print ("Medium password. Try adding a special character for a stronger password")
    elif not (is_lower and is_upper and is_digit and is_special) :
        category = "Medium"
        print ("Medium password. Use a combination of lower and uppercase letters, with number(s) and special character(s).")
    elif is_lower and is_upper and is_digit and is_special :
        category = "Strong"
        print ("Strong password! Great job!")
        password_history.append(password) # store new password

