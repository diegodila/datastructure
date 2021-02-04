import timeit
#11 passos
#function1
def soma1(n):
    soma = 0 
    for i in range(n + 1):
        soma += i
    return soma 

%timeit soma1(10) #gera time de exec

#3 passos 
#function2
def soma2(n):
    return (n * (n + 1)) / 2

%timeit soma2(10)

# a complexidade do algoritmo aumenta com as entradas
# comparativos entre os algoritmos, desempenho de cada uma

# função1 temos uma notação O(n) # muda de acordo com os inputs que recebe 
# função2 temos uma notação O(3) # não muda de acordo com os inputs que recebe