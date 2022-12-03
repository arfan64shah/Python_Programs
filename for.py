Q1
for i in range(10, 21):
    print(i)

Q2
myList = ['Gilgit', 'Ysasin', "Gupis", 'Gahkuch']
myList.append("Bubur")

#print(myList)

#Q3
for i in enumerate(myList):
    print(i)

#Q4
newList = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

Q5
create a list and then convert into set
mylist = [1, 1, 2, 3, 4, 4, 5]
print(mylist)
mySet = set(mylist)
print(mySet)

#now convert back to list
convertedList = list(mySet)
print(convertedList)

Q6
cities = ['Gahkuch', 'Gilgit', 'Yasin']

newCities = ', '.join(cities)
print(newCities)

Q6
myList = [1, 2, 3, 4, 2, 3, 5]

newList = [i for i in myList if i>2]

print(newList)

import numpy as np
print(np.ones([3, 3]))