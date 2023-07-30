import random as rn

def dice():
    for x in range(6):
        result = rn.randint(1, 6)
        return result
print(dice())