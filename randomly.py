import random as rn

try:
    def dice():
        for x in range(6):
            result = rn.randint(1, 6)
            print(result)

    dice()
except Exception as e:
    print(e)