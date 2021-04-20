import random
from credit_card_validator import credit_card_validator

if __name__ == '__main__':
    unittest.main()

def random():
    for x in range(10):
        num = '4'
        for i in range(15):
            digit = str(random.randint(0,9))
            num += digit
        if(not credit_card_validator(num)):
            print("found a bug?")
