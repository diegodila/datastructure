import re
#Function search 
frase = 'Olá, meu numero de telefone é (42)0000-0000'
re.search('\(\d{2}\)\d{4,5}-\d{4}', frase)


frase = 'A placa de carro que eu anotei durante o acidente foi frt-1998'
re.search('[A-Za-z]{3}-\d{4}', frase)

email = 'Entre em contato, meu email é teste@teste.com'
re.search('\w+@\w+\.com',email)

#Function match
frase = 'A placa de carro que eu anotei durante o acidente foi FRT-1998'
print(re.match('[A-Za-z]{3}-\d{4}', frase))

frase2 = 'FRT-1998 é a placa do carro'
print(re.match('[A-Za-z]{3}-\d{4}', frase2))


#Function findall
frase3 = 'Meu número de telefone atual é (42)0000-0000. O número (56)1111-1111 é o antigo'
re.findall('\(\d{2}\)\d{4,5}-\d{4}', frase3)

emails = '''Nome: Teste 1 
emails: teste1@teste.com
Nome: Teste 2 
email: teste2@teste.com
Nome: Teste 3 
email: teste3@teste.com.br'''

re.findall('\w+@\w+\.\w*', emails)