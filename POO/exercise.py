class Studant: 
    def __init__(self,name,grade1, grade2):
        self.name = name 
        self.grade1 = grade1
        self.grade2 = grade2
        self.mean = 0

    def mean_calculate(self):
        self.mean = (self.grade1 + self.grade2) / 2
        return self.mean
   
    def data_show(self):
        print('Name: ',self.name)
        print('Grade 1: ',self.grade1)
        print('Grade 2: ',self.grade2)
        print('Mean: ', self.mean)

    def result(self):
        if self.mean >= 6.0:
            print('aprovado')
        else:
            print('reprovado')


st = Studant('José', 10, 4)
st.mean_calculate()
st.data_show()
st.result()
st1 = Studant('Pedro', 2.5, 6.7)
st1.mean_calculate()
st.data_show()
st.result()