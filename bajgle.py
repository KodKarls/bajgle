import random

import constants


def greet(message) -> None:
    print(message)


def get_secret_character_string() -> str:
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    characters = ['a', 'b', 'c', 'd', 'e', 'f']

    random.shuffle(numbers)
    random.shuffle(characters)

    character_string = ''
    for i in range(constants.NUM_DIGITS):
        character_string += str(numbers[i])
    for i in range(constants.NUM_LETTERS):
        character_string += characters[i]

    return character_string


if __name__ == '__main__':
    print(constants.MESSAGE)
    secret_character_string = get_secret_character_string()
    print(secret_character_string)
