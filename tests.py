import random
import unittest
from credit_card_validator import credit_card_validator


class TestCase(unittest.TestCase):

    # Valid Visa
    def test1(self):
        for i in range(10000):
            visa = visaGen()
            credit_card_validator(visa)

    # Valid Mastercard
    def test2(self):
        for i in range(10000):
            master = masterGen()
            credit_card_validator(master)

    # Valid MasterCard 2
    def test3(self):
        for i in range(10000):
            masterTwo = masterGen2()
            credit_card_validator(masterTwo)

    # Valid AMEX
    def test4(self):
        for i in range(10000):
            amex = amexGen()
            credit_card_validator(amex)

    # 16 Digit Invalid Prefix
    def test5(self):
        for i in range(10000):
            invalid = invalidPref('1')
            credit_card_validator(invalid)
        for i in range(10000):
            invalid = invalidPref('8')
            credit_card_validator(invalid)

    # 15 digit Invalid prefix
    def test6(self):
        for i in range(10000):
            invalShort = invalidPrefShort('1')
            credit_card_validator(invalShort)
        for i in range(10000):
            invalShort = invalidPrefShort('8')
            credit_card_validator(invalShort)

    # Invalid luhn
    def test7(self):
        for i in range(10000):
            invalShort = invalidPrefShort('4')
            invalShort += str(random.ranint(0, 9))
            credit_card_validator(invalShort)
        for i in range(10000):
            invalShort = invalidPrefShort('3')
            invalShort += str(random.ranint(0, 9))
            credit_card_validator(invalShort)

    # Random numbers
    def test8(self):
        for i in range(100000):
            randomNum = completelyRandom()
            credit_card_validator(randomNum)


# Generates completely random numbers with in a range of sizes
def completelyRandom():
    val = str(random.randint(1000000000000, 10000000000000000))
    return val


# Generates 16 digit with wrong prefix
def invalidPref(inp):
    val = inp
    val += str(random.randint(10000000000000, 99999999999999))
    val += str(luhn(val))
    return val


# Generates 15 digit with wrong prefix
def invalidPrefShort(inp):
    val = inp
    val += str(random.randint(1000000000000, 9999999999999))
    val += str(luhn(val))
    return val


# Generates Valid Visa
def visaGen():
    val = '4'
    val += str(random.randint(10000000000000, 99999999999999))
    val += str(luhn(val))
    return val


# Generates Valid MasterCard
def masterGen():
    val = '5'
    val += str(random.randint(10000000000000, 59999999999999))
    val += str(luhn(val))
    return val


# Generates Valid MasterCard
def masterGen2():
    val = '2'
    val += str(random.randint(22100000000000, 72099999999999))
    val += str(luhn(val))
    return val


# Generates Valid Amex
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
