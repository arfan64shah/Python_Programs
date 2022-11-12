import numpy as np

fruits = ["apples", "pears", "grapes"]

vegetables = ["tomato", "potato", "onion"]

fruits.append("peach")

# print(fruits)

fruits.insert(0, "banana")

# print(fruits)

#print(fruits.index("pears"))
#print("pears" in fruits)
#print(type(fruits))

array = np.array([1, 2, 3, 4, 5, 6])
#print(array)
#print(type(array))

#range function 

even_numbers = list(range(0, 100, 2))
print(even_numbers)

count = 0
while(count <= 10):
    print(count)
    count+=1


do {
    print(count)
    count+=1
}while(count <= 10)