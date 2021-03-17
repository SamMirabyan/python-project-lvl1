#!/usr/bin/env python3
import prompt


def main():
    print("Welcome to the Brain Games!")
    user_name = prompt.string('May I have your name? ')
    print(f"Hello, {user_name.title()}!")


if __name__ == '__main__':
    main()
