import unittest
import change_text


class TestChangeText(unittest.TestCase):

    def test_uppercase(self):
        word = "good evening"
        outcome = change_text.uppercase(word)
        self.assertEqual(outcome, 'Good Evening')


if __name__ == '__main__':
    unittest.main()
