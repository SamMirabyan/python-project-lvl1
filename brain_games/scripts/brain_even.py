#!/usr/bin/env python3
from random import randint
from brain_games.scripts import brain_games


user_name = brain_games.main()


def greeting():
    # Greet user once at the start
    print('Answer "yes" if the number is even, otherwise answer "no".')


def random_number():
    # Select random number
    rand_number = randint(0, 1000)
    return rand_number


def is_even(number):
    return 'yes' if number % 2 == 0 else 'no'


def user_input():
    user_input = input("Your answer: ")
    return user_input


def is_correct(answer_1, answer_2):
    # answer_1 == correct answer; answer_2 == user's answer
    return True if answer_1 == answer_2 else False


def game_logic():
    greeting()
    user_points = 0
    correct_answer = ''
    while user_points < 3:
        target_number = random_number()
        print(f'Question: {target_number}')
        correct_answer = is_even(target_number)
        user_answer = user_input()
        if is_correct(correct_answer, user_answer):
            print('Correct!')
            user_points += 1
            continue
        else:
            print((f"'{user_answer}' is wrong answer ;(. Correct answer"
                  f"was '{correct_answer}'.\nLet's try again {user_name}!"))
            break
    if user_points == 3:
        print(f'Congratulations, {user_name}!')


def main():
    game_logic()


if __name__ == '__main__':
    main()
