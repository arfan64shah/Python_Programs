import numpy as np

a = np.array([[1,2,3,4], [2,3,4,5], [3,4,5,6], [4,5,6,7], [5,6,7,8]])


# normalize
amax, amin = a.max(), a.min()
d = (a - amin)/(amax - amin)
print(d)