# """Funchions for brain_games"""

import prompt


def welcome_user():
    """Greeting new user"""
    print('Welcome to Brain Games!')
    name_user = prompt.string('May I know your name?\n')
    print(f'Nice to meet you, {name_user}!')
