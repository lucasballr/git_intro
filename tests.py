import random
import unittest
from credit_card_validator import credit_card_validator


class TestCase(unittest.TestCase):

    # Valid Visa
    def test1(self):
        for i in range(100):
            visa = visaGen()
            credit_card_validator(visa)
    
    # Valid Mastercard
    def test2(self):
        for i in range(20):
            master = masterGen()
            credit_card_validator(master)

    # Valid MasterCard 2
    def test3(self):
        for i in range(20):
            masterTwo = masterGen2()
            credit_card_validator(masterTwo)

    # Valid AMEX
    def test4(self):
        for i in range(20):
            amex = amexGen()
            credit_card_validator(amex)

    # Invalid Pref
    def test5(self):
        for i in range(20):
            invalid = invalidPref('1')
            credit_card_validator(invalid)
        for i in range(20):
            invalid = invalidPref('8')
            credit_card_validator(invalid)

    def test6(self):
        for i in range(20):
            invalShort = invalidPrefShort('1')
            credit_card_validator(invalid)
        for i in range(20):
            invalShort = invalidPrefShort('8')
            credit_card_validator(invalid)


def invalidPref(inp):
    val = inp
    val += str(random.randint(10000000000000, 99999999999999))
    val += str(luhn(val))
    return val

def invalidPrefShort(inp):
    val = inp
    val += str(random.randint(1000000000000, 9999999999999))
    val += str(luhn(val))
    return val

def visaGen():
    val = '4'
    val += str(random.randint(10000000000000, 99999999999999))
    val += str(luhn(val))
    return val

def masterGen():
    val = '5'
    val += str(random.randint(10000000000000, 59999999999999))
    val += str(luhn(val))
    return val

def masterGen2():
    val = '2'
    val += str(random.randint(22100000000000, 72099999999999))
    val += str(luhn(val))
    return val

def amexGen():
    val = '3'
    val += str(random.randint(4000000000000, 7999999999999))
    val += str(luhn(val))
    return val

# Luhn Calculation
def luhn(val):
    digits = len(val)
    sum = 0
    for i in range(digits):
        add = 0
        if (i % 2 == 0):    
            add = int(val[digits - i - 1]) * 2
        else:
            add = int(val[digits - i - 1])
        if add > 9:
            add -= 9
        sum += add
    mod = sum % 10
    check_sum = 0 if mod == 0 else (10 - mod)
    return check_sum

if __name__ == '__main__':
    unittest.main()
