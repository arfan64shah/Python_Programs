import numpy as np
Media_pesos=80
pesos= np.array([72, 35, 64, 88, 51, 90, 74, 12])
def corigir(pes):
    medi = pes.mean()
    print('mean weight= ',medi)
    change = Media_pesos - medi
    print('desired difference',change)
    target= pesos + change
    print(target)
    return np.clip(target, pesos, 95)
print(corigir(pesos))