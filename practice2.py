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

L = [(x, y) for x in [3, 5, 6] for y in [10, 15, 25] if y>3*x]

print(L)

s = {x for x in 'blabla na aula' if x not in ['a', 'f']}
print(s)
print(type(s))

a = (1, 3, 4, 5, 6)
b = (a, a, 3)
print(b)
print(type(b))