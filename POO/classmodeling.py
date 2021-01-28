class Television:
    def __init__(self):
        self.ligada=False
        self.canal=2


tv = Television()
tv.ligada
tv.canal
tvsala = Television()
tvsala.ligada = True
tvsala.canal=4
tv.canal
tvsala.canal
tvsala.ligada


class Car:
    def __init__(self):
        self.ligada = True 
        self.canal = 0


carro = Car()
carro.ligada = 3
carro.ligada