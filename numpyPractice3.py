import numpy as np
arr = np.arange(12)
print(arr)
print(arr.shape)

arr1 = arr.reshape(4, 3)
print(arr1)

swap = np.swapaxes(arr1, 0,1)
print("swap axes is ",swap)