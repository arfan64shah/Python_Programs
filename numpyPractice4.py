import numpy as np
arr = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

print(arr)
print("Max is ", arr.max())
print("max in 1 axis is ", arr.max(axis=1))

print(arr[2].max())
print(arr[0][1])
print(arr[:, 2])

print(arr[:, [0, 1, 2]].max())
print(arr[1:4, 0:2])