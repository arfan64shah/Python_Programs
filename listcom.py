# here i will show you list comprehension
l = []

for i in range(1, 101, 2):
    l.append(i)
print(l)


# list comprehension
m = [n for n in range(1, 101) if n % 2 == 0]
print(m)