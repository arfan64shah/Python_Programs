#swap without using a temporary variable
a = 4
b = 6

a, b = b, a
print(a, b)


#swap using third variable
c = 9
d = 2

temp = c

c = d
d = temp
print(c, d)