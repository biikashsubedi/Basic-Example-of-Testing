import unittest
import games


class TestGame(unittest.TestCase):
    def setUp(self) -> None:
        print('Tested by Bikash Subedi')

    def test_imput_correct(self):
        result = games.run_guess(5, 5)
        self.assertTrue(result)

    def test_input_wrong_guess(self):
        result = games.run_guess(5, 0)
        self.assertFalse(result)

    def test_input_wrong_number(self):
        result = games.run_guess(5, 11)
        self.assertFalse(result)

    def tearDown(self) -> None:
        print()

if __name__ == '__main__':
    unittest.main()