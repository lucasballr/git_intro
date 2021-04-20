import random
import unittest
from credit_card_validator import credit_card_validator

class TestCase(unittest.TestCase):
    def test1(self):
        val = '101'
        self.assertFalse(credit_card_validator(val), msg='{} does not meet requirements'.format(val))
    def test2(self):
        val = '4535893340572712'
        self.assertTrue(credit_card_validator(val), msg='{} does not meet requirements'.format(val))

if __name__ == '__main__':
    unittest.main()
