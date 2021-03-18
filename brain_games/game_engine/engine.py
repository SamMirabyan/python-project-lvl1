import prompt

MAX_POINTS = 3


def is_correct(correct_answer, user_answer):
    return True if correct_answer == user_answer else False


def run_game(game):
    print('Welcome to the Brain Games!')
    user_name = prompt.string('May I have your name? ').title()
    print(f"Hello, {user_name}!")
    print(game.GAME_DESCRIPTION)
    user_points = 0
    while user_points < MAX_POINTS:
        correct_answer = game.get_result()
        user_answer = game.get_user_input()
        if is_correct(correct_answer, user_answer):
            print('Correct!')
            user_points += 1
            continue
        else:
            print((f"'{user_answer}' is wrong answer ;(. Correct answer"
                  f" was '{correct_answer}'.\nLet's try again, {user_name}!"))
            break
    if user_points == 3:
        print(f'Congratulations, {user_name}!')
