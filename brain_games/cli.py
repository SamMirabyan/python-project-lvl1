import prompt


def welcome_user():
    user_name = prompt.string('May I have your name? ')
    print(f"Hello, {user_name.title()}!")
    return user_name.title()
    