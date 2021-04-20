import random
import unittest
from credit_card_validator import credit_card_validator

class TestCase(unittest.TestCase):
    ## Random short number
    def test1(self):
        val = '12341'
        self.assertFalse(credit_card_validator(val), msg='{} does not meet requirements'.format(val))
    ## Valid Visa
    def test2(self):
        val = '4535893340572712'
        self.assertTrue(credit_card_validator(val), msg='{} does not meet requirements'.format(val))
    ## Valid MasterCard
    def test3(self):
        val = '5372076718012718'
        self.assertTrue(credit_card_validator(val), msg='{} does not meet requirements'.format(val))
    ## Valid AMEX
    def test4(self):
        val = '349852453816112'
        self.assertTrue(credit_card_validator(val), msg='{} does not meet requirements'.format(val))
    ## Amex that is too long
    def test5(self):
        val = '3498524538161122'
        self.assertFalse(credit_card_validator(val), msg='{} does not meet requirements'.format(val))
    ## MasterCard with wrong Luhn#
    def test6(self):
        val = '5372076718012717'
        self.assertFalse(credit_card_validator(val), msg='{} does not meet requirements'.format(val))
    ## Visa with wrong Luhn#
    def test7(self):
        val = '4535893340572713'
        self.assertTrue(credit_card_validator(val), msg='{} does not meet requirements'.format(val))
    ## Visa that is too short
    def test8(self):
        val = '453589334057271'
        self.assertFalse(credit_card_validator(val), msg='{} does not meet requirements'.format(val))
    ## MasterCard that is too short
    def test9(self):
        val = '537207671801271'
        self.assertFalse(credit_card_validator(val), msg='{} does not meet requirements'.format(val))
    ## MasterCard that is too long
    def test10(self):
        val = '53720767180127186'
        self.assertFalse(credit_card_validator(val), msg='{} does not meet requirements'.format(val))
    ## Visa that is too long
    def test11(self):
        val = '45358933405727123'
        self.assertFalse(credit_card_validator(val), msg='{} does not meet requirements'.format(val))
    ## Invalid prefix (High)
    def test12(self):
        val = '9535893340572712'
        self.assertFalse(credit_card_validator(val), msg='{} does not meet requirements'.format(val))
    ## Invalid prefix (Low)
    def test13(self):
        val = '2535893340572712'
        self.assertFalse(credit_card_validator(val), msg='{} does not meet requirements'.format(val))
    ## Blank string
    def test14(self):
        val = ''
        self.assertEqual(credit_card_validator(val), False)
    ## Not numbers
    def test15(self):
        val = 'asdfasdfasdfasdf'
        self.assertEqual(credit_card_validator(val), False)
    ## Amex that is too short
    def test16(self):
        val = '34985245381611'
        self.assertFalse(credit_card_validator(val), msg='{} does not meet requirements'.format(val))
    ## Amex with wrong prefix (Low)
    def test17(self):
        val = '339852453816112'
        self.assertFalse(credit_card_validator(val), msg='{} does not meet requirements'.format(val))
    ## Amex with wrong prefix (High)
    def test18(self):
        val = '389852453816112'
        self.assertFalse(credit_card_validator(val), msg='{} does not meet requirements'.format(val))
    

if __name__ == '__main__':
    unittest.main()
