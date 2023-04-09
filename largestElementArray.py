import array as arr
#solved using two methods

#solve using a normal way
arr = arr.array('i', [44, 200, 3, 4, 5, 6, 7, 800])

largest = arr[0]

for i in range(1, len(arr)):
    if arr[i] > largest:
        largest = arr[i]
print(largest)

#solve using function
def largestNum(arr1):
    largest = arr1[0]
    for i in range(1, len(arr1)):
        if arr1[i] > largest:
            largest = arr1[i]
    return largest
arr1 = arr.array('i', [23000, 45, 65, 87, 90, 777, 888, 9999])

print("The largest element in the array is ", largestNum(arr1))
