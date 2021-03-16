from random import randint

GAME_DESCRIPTION = ('Answer "yes" if given number is prime.'
                    'Otherwise answer "no".'
                    )


def get_result():
    rand_number = randint(1, 50)
    divisor_list = [n for n in range(1, rand_number + 1)
                    if rand_number % n == 0]
    print(f"Question: {rand_number}")
    return 'yes' if len(divisor_list) <= 2 else 'no'


def get_user_input():
    user_input = input("Your answer: ")
    return user_input.lower()
