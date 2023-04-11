import array as arr
import sys
ar = arr.array('i', [1, 2, 3, 4, 5, 6, 7, 8])

print(ar[::])

lst = [1, 2, 3, 4, 5, 6, 7, 8]
print(lst[::-2])

print(4 + 6 % 5)

i = 1
while True:
    if i%3 == 0 :
        break
    print(i)
 
    i += 1

i = 0
while i < 5:
    print(i)
    i += 1
    if i == 3:
        break
else:
    print(0)