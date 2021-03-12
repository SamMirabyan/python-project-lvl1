from random import choice, randint
import operator

GAME_DESCRIPTION = 'What is the result of the expression?'
OPERATORS = {'+': operator.add, '*': operator.mul, '-': operator.sub}
KEYS = list(OPERATORS)


def get_result():
    number_1 = randint(1, 20)
    number_2 = randint(1, 10)
    operator = choice(KEYS)
    result = (OPERATORS[operator](number_1, number_2))
    print(f"Question: {number_1} {operator} {number_2}")
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
