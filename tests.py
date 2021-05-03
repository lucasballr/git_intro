import random
import unittest
from credit_card_validator import credit_card_validator


class TestCase(unittest.TestCase):

    # Valid Visa
    def test1(self):
        val = '4'
        val += str(random.randint(10000000000000, 99999999999999))
        val += str(luhn(val))
        self.assertTrue(credit_card_validator(val), msg='incorrect')
    
    # Valid Mastercard
    def test2(self):
        val = '5'
        val += str(random.randint(10000000000000, 59999999999999))
        val += str(luhn(val))
        self.assertTrue(credit_card_validator(val), msg='incorrect')

    # Valid MasterCard 2
    def test3(self):
        val = '2'
        val += str(random.randint(22100000000000, 72099999999999))
        val += str(luhn(val))
        self.assertTrue(credit_card_validator(val), msg='incorrect')

    # Valid AMEX
    def test4(self):
        val = '3'
        val += str(random.randint(4000000000000, 7999999999999))
        val += str(luhn(val))
        self.assertTrue(credit_card_validator(val), msg='incorrect')

# Luhn Calculation
def luhn(val):
    digits = len(val)
    sum = int(val[digits - 1])
    par = digits % 2 
    for i in range(digits):
        if (int(i) % 2 == par):
            i = int(i) * 2
        sum += i
    return (sum % 10)

if __name__ == '__main__':
    unittest.main()
