import numpy as np

fruits = ["apples", "pears", "grapes"]

vegetables = ["tomato", "potato", "onion"]

fruits.append("peach")

# print(fruits)

fruits.insert(0, "banana")

# print(fruits)

print(fruits.index("pears"))
print("pears" in fruits)
print(type(fruits))

array = np.array([1, 2, 3, 4, 5, 6])
print(array)
print(type(array))