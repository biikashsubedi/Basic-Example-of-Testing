import unittest
import adding_math


class TestMain(unittest.TestCase):
    def setUp(self) -> None:
        print('Tested by Bikash Subedi')

    def testt_add(self):
        test_param = 10
        result = adding_math.add(test_param)
        self.assertEqual(result, 15)

    def test_add2(self):
        test_param = 'bikki'
        result = adding_math.add(test_param)
        self.assertIsInstance(result, ValueError)

    def test_add3(self):
        test_param = None
        result = adding_math.add(test_param)
        self.assertEqual(result, 'Please Enter a Number!')

    def tearDown(self) -> None:
        print('Cleaning Up!!')

if __name__ == '__main__':
    unittest.main()