import unittest
import main

class TestPassChecker(unittest.TestCase):
    def test_pass_checker(self):
        test_pass = "123ggg5689"
        result = main.check_pass_validity(test_pass)
        self.assertTrue(result == True)

unittest.main()
