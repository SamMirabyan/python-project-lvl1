#!/usr/bin/env python3
from random import choice, randint
import operator
from brain_games.scripts import brain_games


user_name = brain_games.main()
operators = {'+': operator.add, '*': operator.mul, '-': operator.sub}
keys = list(operators)


def greeting():
    # Greet user once at the start
    print('What is the result of the expression?')


def ask_question(number_1, number_2, operator):
    # Take two numbers and operator, count mathematical expression and show it
    result = (operators[operator](number_1, number_2))
    print(f"Question: {number_1} {operator} {number_2}")
    return result


def is_integer(number):
    # A helper function
    try:
        int(number)
        return True
    except ValueError:
        return False


def user_input():
    user_input = input("Your answer: ")
    if is_integer(user_input):
        return int(user_input)
    else:
        print("Error! This program works only with integers!")
        return user_input


def is_correct(correct_answer, user_answer):
    return True if correct_answer == user_answer else False


def game_logic():
    greeting()
    user_points = 0
    correct_answer = ''
    while user_points < 3:
        number_1 = randint(0, 100)
        number_2 = randint(1, 50)
        random_operator = choice(keys)
        correct_answer = ask_question(number_1, number_2, random_operator)
        user_answer = user_input()
        if is_correct(correct_answer, user_answer):
            print('Correct!')
            user_points += 1
            continue
        else:
            print((f"'{user_answer}' is wrong answer ;(. Correct answer"
                  f" was '{correct_answer}'.\nLet's try again {user_name}!"))
            break
    if user_points == 3:
        print(f'Congratulations, {user_name}!')


def main():
    game_logic()


if __name__ == '__main__':
    main()
