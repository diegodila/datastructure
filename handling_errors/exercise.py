lista = []
try:
    lista.append(float(input('Digite o primeiro valor: ')))
    lista.append(float(input('Digite o segundo valor: ')))
    divisao = lista[0] / lista[1]
except ValueError:
    print('Voce digitou um caracter')
except ZeroDivisionError:
    print('Voce digitou zero, impossivel fazer uma divisão por zero')
except IndexError:
    print('A posicão da lista não pode ser dividida')
except KeyboardInterrupt:
    print('O usuário interrompeu a execução')
else:
    print(f'A divisão de {lista[0]} por {lista[1]} é: {divisao}')