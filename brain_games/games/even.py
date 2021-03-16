from random import randint

GAME_DESCRIPTION = ('Answer "yes" if given number is even.'
                    'Otherwise answer "no".'
                    )


def get_result():
    rand_number = randint(1, 1000)
    print(f"Question: {rand_number}")
    return 'yes' if rand_number % 2 == 0 else 'no'


def get_user_input():
    user_input = input("Your answer: ")
    return user_input.lower()
