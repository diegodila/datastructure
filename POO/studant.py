class Studant:
    def __init__(self, name, grade1, grade2):
        self.name = name
        self.grade1 = grade1
        self.grade2 = grade2

    def meanstudant(self):
        return (self.grade1 + self.grade2) / 2


studant = Studant("Diego",10, 10)
print(studant.name)
print(studant.meanstudant())