numbers = [2, 3, 4, 5, 6]

numbers.insert(0, 10)

numbers.sort(reverse=False)

print(numbers)

names = ['Zulfiqar', 'Tajwar', 'Munner', 'Jahangir']

for i in names:
    if (i == 'Munner'):
        print("Found", i, "at index", names.index(i))
        break