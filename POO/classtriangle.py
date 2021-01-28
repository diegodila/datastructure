class Triangle:
    def __init__(self, side1, side2, side3, base, height):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3
        self.base = base
        self.height = height

    def area(self):
        return (self.base * self.height) / 2

    def tipo(self):
        if self.side1 > self.side2 + self.side3:
            return 'This is not a Triangle'
        elif self.side1 == self.side2 and self.side1 == self.side3:
            return 'Triangle Isóceles'
        else:
            return 'Another type of Triangle'

t1 = Triangle(2, 2, 2, 4, 3)
print(t1.side1,t1.side2, t1.side3,t1.base, t1.height)
t1.area()
t1.tipo()

t2 = Triangle(8,8,8,16,9)
print(t2.side1,t2.side2,t2.side3,t2.base, t2.height)
t2.area()
t2.tipo()