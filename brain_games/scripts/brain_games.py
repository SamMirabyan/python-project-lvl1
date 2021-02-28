#!/usr/bin/env python3
import os
import os.path
import sys

sys.path.append(os.getcwd() + "\\brain_games")
from brain_games import cli


def main():
    print("Welcome to the Brain Games!")
    cli.welcome_user()


if __name__ == '__main__':
    main()
