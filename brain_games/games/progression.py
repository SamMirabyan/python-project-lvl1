from random import randint

GAME_DESCRIPTION = "What number is missing in the progression?"


def get_result():
    rand_mult = randint(1, 20)
    progression = [x * rand_mult for x in range(rand_mult, rand_mult + 10)]
    target_index = randint(0, 9)
    replaced_element = progression.pop(target_index)
    progression.insert(target_index, '..')
    print('Question: ', end='')
    for element in progression:
        print(element, end=' ')
    return replaced_element


def is_integer(number):
    # A helper function
    try:
        int(number)
        return True
    except ValueError:
        return False


def get_user_input():
    user_input = input("\nYour answer: ")
    if is_integer(user_input):
        return int(user_input)
    else:
        print("Error! This program works only with integers!")
        return user_input
