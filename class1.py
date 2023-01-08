class point:
    def reset(self):
        self.x = 0
        self.y = 0
    
    def point1(p1):
        p1.x = 2
        p1.y = 3
        

p = point()
p.point1()
p.reset()

print(p.x, p.y)
