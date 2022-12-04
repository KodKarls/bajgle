import itertools
import unittest

import game_functions
import constants


def get_all_permutation(numbers_and_characters: list) -> list[tuple[str]]:
    return list(itertools.permutations(numbers_and_characters, constants.LENGTH_PERMUTATION))


def get_needed_permutation(permutation_list: list[tuple[str]]) -> list[str]:
    result = []

    for permutation_tuple in permutation_list:
        if check_permutation(permutation_tuple):
            result.append(prepare_needed_permutation(permutation_tuple))

    return result


def check_permutation(tup: tuple[str]) -> bool:
    for i in range(constants.NUM_DIGITS):
        if tup[i] not in constants.NUMBERS_LIST:
            return False
    for i in range(constants.NUM_DIGITS, constants.LENGTH_SECRET_STRING):
        if tup[i] not in constants.LETTERS_LIST:
            return False

    return True


def prepare_needed_permutation(tup: tuple[str]) -> str:
    character_string = ''

    for s in tup:
        character_string += str(s)

    return character_string


class BajgleGameTestCase(unittest.TestCase):

    def test_get_secret_character_string(self):
        numbers_and_characters = constants.NUMBERS_LIST + constants.LETTERS_LIST
        all_permutation = get_all_permutation(numbers_and_characters)
        all_secret_strings = get_needed_permutation(all_permutation)

        random_secret_character_string = game_functions.get_secret_character_string()

        self.assertIn(random_secret_character_string, all_secret_strings)

    def test_correct_user_input(self):
        user_input = '173abc'

        result = game_functions.validate_input(user_input)

        self.assertEqual(result, True)

    def test_incorrect_user_input(self):
        user_input = 'abc278'

        result = game_functions.validate_input(user_input)

        self.assertEqual(result, False)

    def test_get_piko_clue(self):
        guess = '123abc'
        secret_string = '415def'

        clue = game_functions.get_clues(guess, secret_string)

        self.assertEqual(clue, constants.PIKO_MESSAGE)

    def test_get_fermi_clue(self):
        guess = '123abc'
        secret_string = '145def'

        clue = game_functions.get_clues(guess, secret_string)

        self.assertEqual(clue, constants.FERMI_MESSAGE)

    def test_get_bajgle_clue(self):
        guess = '123abc'
        secret_string = '456def'

        clue = game_functions.get_clues(guess, secret_string)

        self.assertEqual(clue, constants.BAJGLE_MESSAGE)

    def test_get_win_clue(self):
        guess = '123abc'
        secret_string = '123abc'

        clue = game_functions.get_clues(guess, secret_string)

        self.assertEqual(clue, constants.WIN_MESSAGE)


if __name__ == '__main__':
    unittest.main()
