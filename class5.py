# create a class named human
class Human:
    # define first method
    def __init__(self, name, sex, age):
        self.name = name
        self.sex = sex
        self.age = age
    
    # define another method
    def works(self):
        if (self.name == 'arfan shah'):
            print(self.name, "is Data Scientist")
        else:
            print("Please put a valid name!")
    
    # define one more function
    def eats(self):
        if (self.age == 'male'):
            print("Males loved to eat beef!")
arfan = Human('arfan shah', 27, 'male')
arfan.works()
arfan.eats()