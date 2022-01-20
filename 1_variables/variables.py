"""
Variáveis e constantes
Por meio de variáveis que um algortimo “guarda” os dados do problema
Todo dado que tem a possibilidade de ser alterado no decorrer do tempo deverá ser tratado como uma variável
Quando um dado não tem nenhuma possibilidade de variar no decorrer do tempo, deverá ser tratado como constante
Exemplo: calcular a área de um triângulo. Sabemos que a fórmula para o cálculo da área de um triângulo é BASE * ALTURA / 2. Base e altura são dados que irão variar no decorrer do “tempo de execução”. O número 2 da fórmula é um dado constante, pois sempre terá o mesmo valor

Tipo de variáveis
Inteiros: valores positivos ou negativos, que não possuem uma parte fracionária. Exemplos: 1, 30, 40, 12, -50
Float (real): valores positivos ou negativos, que podem possuir uma parte fracionária (também podem ser inteiros). Exemplos: 1.4, 6.7, 10.3, 100, -47
Caracteres (char ou string): qualquer elemento presente no teclado. Exemplos: “Maria”, “João”, "M","F"
Lógico (boleano): verdadeiro ou falso. Exemplos: true, false, 1, 0

"""

number = 3
game_number = 14
guest_number = 15

print(number)
print(number, guest_number)

# Float variables (ponto flutuante)
pi_number = 3.14
euler_number = 2.71
scale = 4.57

print(f'the PI number is {pi_number}')
print(f'the EULER number  is {euler_number}')
print(f'The scale is {scale}')

## Strings and chars
string_char = 'a'
string_string = ' dolphin'

print(f'{string_char}{string_string}')
print(f'->>>> {string_char}{string_string}')

#input and convert to int, float, string

age = int(input('Type your age:'))
print(f'your age is {age}')

water = float(input('type water lbs: '))
print(f'The water lbs is {water}')

name = str(input('type your name: '))
print(f'your name is {name}')
