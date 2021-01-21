#3 = 4 #Sintaxe error 
#print('meu nome é 'nome) #Name Error variable is not define  
#print(3/0) #Zero division error 
#2.3 / 'cachorro' #Type error (tipo de dado incompativel)
#c = [1,2,3,4,5]
#c[5] # Index error

# Tratamento de erros 
try:
    n = int(input('Digite um numero inteiro:'))
except:
    print('Valor inválido')
else:
    print(f'Valor digitado é {n}')

while True:
    try:
        n = int(input('Digite um numero inteiro:'))
    except:
        print('Valor inválido')
        break
    else:
        print(f'Valor digitado é {n}')

while True:
    try:
        n = int(input('Digite um numero inteiro:'))
    except:
        print('Valor inválido')
    else:
        print(f'Valor digitado é {n}')
        break 

while True:
    try:
        p = int(input('Digite um numero inteiro:'))
    except ValueError:
        print('Valor inválido')
    except KeyboardInterrupt:
        print('Usuário interrompeu a execução')
        break
    else:
        print(f'Valor digitado é {p}')
        break 
