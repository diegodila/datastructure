import timeit

#Function 3
def lista1():
    lista = [] #criamos uma lista 
    for i in range(1000): 
        lista += [i] #incrementamos n vezes na lista
    return lista

print(lista1()) #cria a lista quando chamamos a função
len(lista1)
#%timeit lista1() # retorn 68.3 micros

#function 4
#já cria a lista automaticamente, sem ser manualmente, usando essa estrutura de dados 
def lista2():
    return range(1000)
print(lista2()) #tipo de retorno range  

l = lista2()

for i in l:
    print(i)

#%timeit list2()