name = 55
def myname():
    global name
    name += 2
    print(name)

myname()

print(name)

def add(x, y):
    sum = x+y
    return sum

print(add(2, 3))
