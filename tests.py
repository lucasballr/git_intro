import random
import unittest
from credit_card_validator import credit_card_validator


class TestCase(unittest.TestCase):
    # Random short number
    def test1(self):
        val = '12341'
        self.assertFalse(credit_card_validator(val), msg='incorrect')

    # Valid Visa
    def test2(self):
        val = '4535893340572712'
        self.assertTrue(credit_card_validator(val), msg='incorrect')

    # Valid MasterCard
    def test3(self):
        val = '5372076718012718'
        self.assertTrue(credit_card_validator(val), msg='incorrect')

    # Valid AMEX
    def test4(self):
        val = '349852453816112'
        self.assertTrue(credit_card_validator(val), msg='incorrect')

    # Amex that is too long
    def test5(self):
        val = '3498524538161122'
        self.assertFalse(credit_card_validator(val), msg='incorrect')

    # MasterCard with wrong Luhn#
    def test6(self):
        val = '5372076718012717'
        self.assertFalse(credit_card_validator(val), msg='incorrect')

    # Visa with wrong Luhn#
    def test7(self):
        val = '4535893340572713'
        self.assertTrue(credit_card_validator(val), msg='incorrect')

    # Visa that is too short
    def test8(self):
        val = '453589334057271'
        self.assertFalse(credit_card_validator(val), msg='incorrect')

    # MasterCard that is too short
    def test9(self):
        val = '537207671801271'
        self.assertFalse(credit_card_validator(val), msg='incorrect')

    # MasterCard that is too long
    def test10(self):
        val = '53720767180127186'
        self.assertFalse(credit_card_validator(val), msg='incorrect')

    # Visa that is too long
    def test11(self):
        val = '45358933405727123'
        self.assertFalse(credit_card_validator(val), msg='incorrect')

    # Visa Invalid prefix (High)
    def test12(self):
        val = '9535893340572712'
        self.assertFalse(credit_card_validator(val), msg='incorrect')

    # Visa Invalid prefix (Low)
    def test13(self):
        val = '2535893340572712'
        self.assertFalse(credit_card_validator(val), msg='incorrect')

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
        self.assertFalse(credit_card_validator(val), msg='incorrect')

    # Amex with wrong prefix (Low)
    def test17(self):
        val = '339852453816112'
        self.assertFalse(credit_card_validator(val), msg='incorrect')

    # Amex with wrong prefix (High)
    def test18(self):
        val = '389852453816112'
        self.assertFalse(credit_card_validator(val), msg='incorrect')

    # AMEX with wrong Luhn#
    def test19(self):
        val = '349852453816110'
        self.assertFalse(credit_card_validator(val), msg='incorrect')

    # Invalid MasterCard prefix (low)
    def test20(self):
        val = '5072076718012718'
        self.assertFalse(credit_card_validator(val), msg='incorrect')

    # Invalid MasterCard prefix (High)
    def test21(self):
        val = '562076718012718'
        self.assertFalse(credit_card_validator(val), msg='incorrect')

    # Wrong Type
    def test22(self):
        val = 4535893340572712
        self.assertFalse(credit_card_validator(val), msg='incorrect')

    # Visa with correct checksum but short
    def test23(self):
        val = '457539185277329'
        self.assertFalse(credit_card_validator(val), msg='incorrect')

    # Visa with correct checksum but long
    def test24(self):
        val = '45753918527732587'
        self.assertFalse(credit_card_validator(val), msg='incorrect')

    # MasterCard with correct checksum but short
    def test25(self):
        val = '557429628000851'
        self.assertFalse(credit_card_validator(val), msg='incorrect')

    # MasterCard with correct checksum but long
    def test26(self):
        val = '55742962800085811'
        self.assertFalse(credit_card_validator(val), msg='incorrect')

    # AMEX with correct checksum but short
    def test27(self):
        val = '34989070718048'
        self.assertFalse(credit_card_validator(val), msg='incorrect')

    # AMEX with correct checksum but long
    def test28(self):
        val = '3498907071804719'
        self.assertFalse(credit_card_validator(val), msg='incorrect')

    # Valid luhn Wrong prefix 1
    def test29(self):
        val = '2220542735795487'
        self.assertFalse(credit_card_validator(val), msg='incorrect')

    # Valid luhn Wrong prefix 2
    def test30(self):
        val = '2721542735795481'
        self.assertFalse(credit_card_validator(val), msg='incorrect')

    # Valid luhn Wrong prefix 3
    def test31(self):
        val = '339890707180473'
        self.assertFalse(credit_card_validator(val), msg='incorrect')

    # Valid luhn Wrong prefix 4
    def test32(self):
        val = '389890707180472'
        self.assertFalse(credit_card_validator(val), msg='incorrect')

    # Valid luhn right prefix
    def test33(self):
        val = '4075391852773253'
        self.assertTrue(credit_card_validator(val), msg='incorrect')

    # Valid luhn Wrong prefix 5
    def test34(self):
        val = '3975391852773256'
        self.assertFalse(credit_card_validator(val), msg='incorrect')

    # Valid luhn Wrong prefix 6
    def test35(self):
        val = '5075391852773250'
        self.assertFalse(credit_card_validator(val), msg='incorrect')

    # Valid luhn Wrong prefix 7
    def test36(self):
        val = '5675391852773254'
        self.assertFalse(credit_card_validator(val), msg='incorrect')

    # Valid in prefix range 2221-2720
    def test37(self):
        val = '2222457385962865'
        self.assertTrue(credit_card_validator(val), msg='incorrect')

    # Valid AMEX
    def test38(self):
        val = '370008845867063'
        self.assertTrue(credit_card_validator(val), msg='incorrect')

    # Just zeros
    def test39(self):
        val = '0000000000000000'
        self.assertFalse(credit_card_validator(val), msg='incorrect')

    # Just zeros but less of them
    def test39(self):
        val = '000000000000000'
        self.assertFalse(credit_card_validator(val), msg='incorrect')

    # Valid AMEX with a different way of showing string
    def test38(self):
        self.assertTrue(credit_card_validator(:"37000884"+"5867063"), msg='incorrect')
        

if __name__ == '__main__':
    unittest.main()
