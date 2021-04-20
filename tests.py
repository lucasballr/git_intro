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
    def test3(self):
        val = '5372076718012718'
        self.assertTrue(credit_card_validator(val), msg='{} does not meet requirements'.format(val))
    def test4(self):
        val = '349852453816112'
        self.assertTrue(credit_card_validator(val), msg='{} does not meet requirements'.format(val))
    def test5(self):
        val = '3498524538161122'
        self.assertFalse(credit_card_validator(val), msg='{} does not meet requirements'.format(val))
    def test6(self):
        val = '5372076718012717'
        self.assertFalse(credit_card_validator(val), msg='{} does not meet requirements'.format(val))
    def test7(self):
        val = '4535893340572713'
        self.assertTrue(credit_card_validator(val), msg='{} does not meet requirements'.format(val))
    def test8(self):
        val = '453589334057271'
        self.assertFalse(credit_card_validator(val), msg='{} does not meet requirements'.format(val))
    def test9(self):
        val = '537207671801271'
        self.assertFalse(credit_card_validator(val), msg='{} does not meet requirements'.format(val))
    def test10(self):
        val = '53720767180127186'
        self.assertFalse(credit_card_validator(val), msg='{} does not meet requirements'.format(val))
    def test11(self):
        val = '45358933405727123'
        self.assertFalse(credit_card_validator(val), msg='{} does not meet requirements'.format(val))
    def test2(self):
        val = '9535893340572712'
        self.assertFalse(credit_card_validator(val), msg='{} does not meet requirements'.format(val))

if __name__ == '__main__':
    unittest.main()
