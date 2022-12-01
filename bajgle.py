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


def validate_input(user_input: str) -> bool:
    for i in range(constants.NUM_DIGITS):
        if user_input[i] not in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
            return False

    for i in range(constants.NUM_DIGITS, constants.NUM_DIGITS + constants.NUM_LETTERS):
        if user_input[i] not in ['a', 'b', 'c', 'd', 'e', 'f']:
            return False

    return True


def get_clues(guess: str, secret_string: str) -> str:
    if guess == secret_string:
        return constants.WIN_MESSAGE

    clues = []
    for i in range(len(guess)):
        if guess[i] == secret_string[i]:
            clues.append(constants.FERMI_MESSAGE)
        elif guess[i] in secret_string:
            clues.append(constants.PIKO_MESSAGE)

    if len(clues) == 0:
        return constants.BAJGLE_MESSAGE
    else:
        clues.sort()
        return ' '.join(clues)


if __name__ == '__main__':
    print(constants.MESSAGE)

    while True:
        secret_character_string = get_secret_character_string()
        print('Mam na myśli pewien ciąg znaków.')
        print(f'Masz {constants.MAX_GUESSES} prób, by go odgadnąć.')

        number_of_guesses = 1
        while number_of_guesses <= constants.MAX_GUESSES:
            guess = ''
            while len(guess) != constants.NUM_DIGITS + constants.NUM_LETTERS or not validate_input(guess):
                print(f'Próba #{number_of_guesses}: ')
                guess = input('> ')

            clues = get_clues(guess, secret_character_string)
            print(clues)
            number_of_guesses += 1

            if guess == secret_character_string:
                break
            if number_of_guesses > constants.MAX_GUESSES:
                print('Wykorzystałeś wszystkie próby.')
                print(f'Prawidłowa odpowiedź to: {secret_character_string}')

        print('Czy chcesz zagrać jeszcze raz? (tak lub nie)')
        if not input('> ').lower().startswith('t'):
            break

    print('Dziękuję za grę!')
