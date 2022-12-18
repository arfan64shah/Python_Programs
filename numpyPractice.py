import numpy as np
Media_pesos=90
pesos= np.array([72, 35, 64, 88, 51, 90, 74, 12])
def corigir(pes):
    medi = pes.mean()
    print('mean weight= ',medi)
    change = Media_pesos - medi
    print('desired difference',change)
    target= pesos + change
    print("target is ", target)
    return np.clip(target, pesos, 95)
print(corigir(pesos))

mat=np.array([[1,2,3],[1,2,3]])
print(mat.shape)  #a tuple

vec=np.array([1,2,3])
print(vec.shape)


np1 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
np2 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

print(np1 + np2)
print(np1 + 2)
print(np1.sum())


b = np1[0:2]
print(np1 - b)