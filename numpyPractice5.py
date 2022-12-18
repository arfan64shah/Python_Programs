import numpy as np

square = np.array([
    [16, 3, 2, 13],
    [5, 10, 11, 6],
    [9, 6, 7, 12],
    [4, 15, 14, 1]
])

print(square[1:3, 2:])
print(square[0, :].sum())

for i in range(4):
    if square[:, i].sum() != 34:
        print ("check "+str(i)+" column")
for i in range(4):
    if square[i, :].sum() != 34:
        print("check "+str(i)+" line")

if square[:2, :2].sum() != 34:
    print ('up left wrong')

if square[2:, :2].sum() != 34:
    print ('down left wrong')

if square[:2, 2:].sum() != 34:
    print ('up right wrong')

if square[2:, 2:].sum() != 34:
     print ('down right wrong')