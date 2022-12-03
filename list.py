list = ['python', 'scipy', 2.7]
print(list)

#delete last element
list.pop(-1)
print(list)


#now insert another element
list.insert(2, 'numpy')
print(list[0])

print(list[-1])

#declare a a list inside another list
twoDimensionalList = [[1, 2], [3, 4]]
print(twoDimensionalList[0])
print(twoDimensionalList[1])

print(twoDimensionalList[0][0])

#declare a new list of strings
namesList = ['kiran', 'adiba', 'dibar', 'wajahat', 'amin']
namesList.sort(reverse=True)

print(namesList)

#declare an list and empty list
newList = [1, 2, 3, 4, 5, 6, 7, 8, 9]
squares = []

for i in newList:
    squares.append(i**2)
print(newList)
print(squares)
