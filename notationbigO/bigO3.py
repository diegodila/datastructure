from math import log 
import numpy as np
import matplotlib.pyplot as plt

n = np.linspace(1,10,100) #gerando numeros linearmente, ate 10. imprimindo 100 numeros

len(n)

labels = ['Constant', 'Logarithmic', 'Linear', 'Log linear', 'Quadratic', 'Cubic', 'Exponential']
#simulação de funções e big o
#np.ones() gera numero um, np.ones(100) gera cem numeros 1
#np.log(n) aplica o logaritmo em n
#n função linear
#n * np.log(n) é o log e o linear aplicados a n 
#n**2 exponencial a 2, elevamos ao quadrado 
#n**3 exponencial a 3, elevamos ao cubo
#2**n exponencial de 2 elevado a n

np.ones(2) #cria 2 numeros 1's
big_o = [np.ones(n.shape), np.log(n), n, n * np.log(n), n**2, n**3, 2**n]

#plt.figure cria a figura, com o tamanho definido pela função 
#plt.ylim //limite do eixo y do grafico

plt.figure(figsize=(10,8))
plt.ylim(0,100)
plt.plot(n, big_o[0])

plt.figure(figsize=(10,8))
plt.ylim(0,100)
for i in range(len(big_o)):
    plt.plot(n, big_o[i], label = labels[i])
plt.legend()
plt.ylabel('Runtime')
plt.xlabel('n')