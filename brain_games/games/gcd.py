from random import randint

GAME_DESCRIPTION = 'Find the greatest common divisor of given numbers.'


def get_result():
    number_1 = randint(1, 10) * randint(1, 10)
    number_2 = randint(1, 10) * randint(1, 10)
    divisor_set_1 = {x for x in range(1, number_1 + 1) if number_1 % x == 0}
    divisor_set_2 = {x for x in range(1, number_2 + 1) if number_2 % x == 0}
    result = max(divisor_set_1 & divisor_set_2)
    print(f"Question: {number_1} {number_2}")
    return result


def is_integer(number):
    # A helper function
    try:
        int(number)
        return True
    except ValueError:
        return False


def get_user_input():
    user_input = input("Your answer: ")
    if is_integer(user_input):
        return int(user_input)
    else:
        print("Error! This program works only with integers!")
        return user_input
