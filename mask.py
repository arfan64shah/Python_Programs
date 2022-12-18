import numpy as np

lst = []
for i in range(16):
    lst.append(i)

arr = np.array(lst)
arr.resize(4, 4)
print(arr)


myMask = arr%2 == 0
print(myMask)

arr1 = arr[myMask]
print(arr1)

c = np.array([1,2,3,4,5])
b = np.array([1,4,3,5,6])
r = c[c<b]
print(r)

std=arr.std()
print(std)
b=arr[(arr>std )& (arr<(std+1))]
print(b)
