import random
import unittest
from credit_card_validator import credit_card_validator

if __name__ == '__main__':
    unittest.main()

def random():
    for x in range(10):
        num = '4'
        for i in range(15):
            digit = str(random.randint(0, 9))
            num += digit
        if(not credit_card_validator(num)):
            print("found a bug?")
            return False
    for x in range(10):
        num = '5'
        num += str(random,randint(1, 5))
        for i in range(14):
            digit = str(random.randint(0, 9))
            num += digit
        if(not credit_card_validator(num)):
            print("found a bug?")
            return False
    for x in range(10):
        num = '2'
        num += str(random,randint(221, 720))
        for i in range(12):
            digit = str(random.randint(0, 9))
            num += digit
        if(not credit_card_validator(num)):
            print("found a bug?")
            return False
    for x in range(10):
        num = '3'
        num += str(random,randint(4, 7))
        for i in range(13):
            digit = str(random.randint(0, 9))
            num += digit
        if(not credit_card_validator(num)):
            print("found a bug?")
            return False

def luhn(num):
    total = 0
    for i in range(len(num)):
        if (i % 2 == 1):
            total += int(num[i])
    return ((total * 9) % 10)

def randomLuhn():
    for x in range(10):
        num = '4'
        for i in range(14):
            digit = str(random.randint(0, 9))
            num += digit
        num += str(luhn(num))
        if(not credit_card_validator(num)):
            print("found a bug?")
            return False
    for x in range(10):
        num = '5'
        num += str(random,randint(1, 5))
        for i in range(13):
            digit = str(random.randint(0, 9))
            num += digit
        num += str(luhn(num))
        if(not credit_card_validator(num)):
            print("found a bug?")
            return False
    for x in range(10):
        num = '2'
        num += str(random,randint(221, 720))
        for i in range(11):
            digit = str(random.randint(0, 9))
            num += digit
        num += str(luhn(num))
        if(not credit_card_validator(num)):
            print("found a bug?")
            return False
    for x in range(10):
        num = '3'
        num += str(random,randint(4, 7))
        for i in range(12):
            digit = str(random.randint(0, 9))
            num += digit
        num += str(luhn(num))
        if(not credit_card_validator(num)):
            print("found a bug?")
            return False

random()
randomLuhn()
