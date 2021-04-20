import random
import unittest
from credit_card_validator import credit_card_validator

class TestCase(unittest.TestCase):
    # Random short number
    def test1(self):
        val = '12341'
        self.assertFalse(credit_card_validator(val), msg='{} does not meet requirements'.format(val))
    # Valid Visa
    def test2(self):
        val = '4535893340572712'
        self.assertTrue(credit_card_validator(val), msg='{} does not meet requirements'.format(val))
    # Valid MasterCard
    def test3(self):
        val = '5372076718012718'
        self.assertTrue(credit_card_validator(val), msg='{} does not meet requirements'.format(val))
    # Valid AMEX
    def test4(self):
        val = '349852453816112'
        self.assertTrue(credit_card_validator(val), msg='{} does not meet requirements'.format(val))
    # Amex that is too long
    def test5(self):
        val = '3498524538161122'
        self.assertFalse(credit_card_validator(val), msg='{} does not meet requirements'.format(val))
    # MasterCard with wrong Luhn#
    def test6(self):
        val = '5372076718012717'
        self.assertFalse(credit_card_validator(val), msg='{} does not meet requirements'.format(val))
    # Visa with wrong Luhn#
    def test7(self):
        val = '4535893340572713'
        self.assertTrue(credit_card_validator(val), msg='{} does not meet requirements'.format(val))
    # Visa that is too short
    def test8(self):
        val = '453589334057271'
        self.assertFalse(credit_card_validator(val), msg='{} does not meet requirements'.format(val))
    # MasterCard that is too short
    def test9(self):
        val = '537207671801271'
        self.assertFalse(credit_card_validator(val), msg='{} does not meet requirements'.format(val))
    # MasterCard that is too long
    def test10(self):
        val = '53720767180127186'
        self.assertFalse(credit_card_validator(val), msg='{} does not meet requirements'.format(val))
    # Visa that is too long
    def test11(self):
        val = '45358933405727123'
        self.assertFalse(credit_card_validator(val), msg='{} does not meet requirements'.format(val))
    # Visa Invalid prefix (High)
    def test12(self):
        val = '9535893340572712'
        self.assertFalse(credit_card_validator(val), msg='{} does not meet requirements'.format(val))
    # Visa Invalid prefix (Low)
    def test13(self):
        val = '2535893340572712'
        self.assertFalse(credit_card_validator(val), msg='{} does not meet requirements'.format(val))
    # Blank string
    def test14(self):
        val = ''
        self.assertEqual(credit_card_validator(val), False)
    # Not numbers
    def test15(self):
        val = 'asdfasdfasdfasdf'
        self.assertEqual(credit_card_validator(val), False)
    # Amex that is too short
    def test16(self):
        val = '34985245381611'
        self.assertFalse(credit_card_validator(val), msg='{} does not meet requirements'.format(val))
    # Amex with wrong prefix (Low)
    def test17(self):
        val = '339852453816112'
        self.assertFalse(credit_card_validator(val), msg='{} does not meet requirements'.format(val))
    # Amex with wrong prefix (High)
    def test18(self):
        val = '389852453816112'
        self.assertFalse(credit_card_validator(val), msg='{} does not meet requirements'.format(val))
    # AMEX with wrong Luhn#
    def test19(self):
        val = '349852453816110'
        self.assertFalse(credit_card_validator(val), msg='{} does not meet requirements'.format(val))
    # Invalid MasterCard prefix (low)
    def test20(self):
        val = '5072076718012718'
        self.assertFalse(credit_card_validator(val), msg='{} does not meet requirements'.format(val))
    # Invalid MasterCard prefix (High)
    def test21(self):
        val = '562076718012718'
        self.assertFalse(credit_card_validator(val), msg='{} does not meet requirements'.format(val))
    # Wrong Type
    def test22(self):
        val = 4535893340572712
        self.assertFalse(credit_card_validator(val), msg='{} does not meet requirements'.format(val))
    # Visa with correct checksum but short
    def test23(self):
        val = '457539185277329'
        self.assertFalse(credit_card_validator(val), msg='{} does not meet requirements'.format(val))
    # Visa with correct checksum but long
    def test24(self):
        val = '45753918527732587'
        self.assertFalse(credit_card_validator(val), msg='{} does not meet requirements'.format(val))
    # MasterCard with correct checksum but short
    def test25(self):
        val = '557429628000851'
        self.assertFalse(credit_card_validator(val), msg='{} does not meet requirements'.format(val))
    # MasterCard with correct checksum but long
    def test26(self):
        val = '55742962800085811'
        self.assertFalse(credit_card_validator(val), msg='{} does not meet requirements'.format(val))
    # AMEX with correct checksum but short
    def test27(self):
        val = '34989070718048'
        self.assertFalse(credit_card_validator(val), msg='{} does not meet requirements'.format(val))
    # AMEX with correct checksum but long
    def test28(self):
        val = '3498907071804719'
        self.assertFalse(credit_card_validator(val), msg='{} does not meet requirements'.format(val))
    # Valid luhn Wrong prefix 1
    def test29(self):
        val = '2220542735795487'
        self.assertFalse(credit_card_validator(val), msg='{} does not meet requirements'.format(val))
    # Valid luhn Wrong prefix 2
    def test30(self):
        val = '2721542735795481'
        self.assertFalse(credit_card_validator(val), msg='{} does not meet requirements'.format(val))
    # Valid luhn Wrong prefix 3
    def test31(self):
        val = '339890707180473'
        self.assertFalse(credit_card_validator(val), msg='{} does not meet requirements'.format(val))
    # Valid luhn Wrong prefix 4
    def test32(self):
        val = '389890707180472'
        self.assertFalse(credit_card_validator(val), msg='{} does not meet requirements'.format(val))
    # Valid luhn right prefix
    def test33(self):
        val = '4075391852773253'
        self.assertTrue(credit_card_validator(val), msg='{} does not meet requirements'.format(val))
    # Valid luhn Wrong prefix 5
    def test34(self):
        val = '3975391852773256'
        self.assertFalse(credit_card_validator(val), msg='{} does not meet requirements'.format(val))
    # Valid luhn Wrong prefix 6
    def test35(self):
        val = '5075391852773250'
        self.assertFalse(credit_card_validator(val), msg='{} does not meet requirements'.format(val))
    # Valid luhn Wrong prefix 7
    def test36(self):
        val = '5675391852773254'
        self.assertFalse(credit_card_validator(val), msg='{} does not meet requirements'.format(val))
    
# Valid Visa = 4575391852773258
# Valid MasterCard 5574296280008581
# Valid Amex 349890707180471

if __name__ == '__main__':
    unittest.main()
