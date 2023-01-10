class employee:
    def __init__(self, fname, lname, income):
        self.fname = fname
        self.lname = lname
        self.income = income
        self.email = fname + "." + lname + "@smarttechy.com"

    def fullname(self):
        return '{} {}'.format(self.fname, self.lname)


emp1 = employee('Arfan', 'Shah', 20000)
emp2 = employee('Zulfiqar', 'Azam', 40000)

print(emp2.fullname())