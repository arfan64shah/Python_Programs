lst = []
sqr_lst = []

for i in range(10):
    lst.append(i)

print(lst)

for i in range(10):
    sqr_lst.append(i*i)
print(sqr_lst)

#list comprehension
l = [i*i for i in range(10)]
print(l)