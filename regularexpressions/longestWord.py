import re

emails = '''Nome: Teste 1 
emails: teste1@teste.com
Nome: Teste 2 
email: teste2@teste.com
Nome: Teste 3 
email: teste3@teste.com.br'''

a = re.findall('\w+@\w+\.\w*', emails)
print(a)

test = "fun&!! time"
b = re.findall('[a-zA-Z]+', test)
print(b)

def LongestWord(sen):
    x = re.findall('[a-zA-Z]+', sen)
    result = ''
    for i in x:
        if(len(i) > len(result)):
            result = i
    print(x)
    print(result)
    return result


# keep this function call here 
print(LongestWord("I love dogs"))

# frase2 = 'FRT-1998 é a placa do carro'
# a = re.match('[A-Za-z]{3}-\d{4}', frase2)
# print(a)

# xx = "fun&!! time"
# a = re.findall('[a-zA-Z]+', xx)
# print(len(a[0]))

test_str = "GeeksforGeeks"
      
all_freq = {}
for i in test_str:
    if i in all_freq:
        all_freq[i] += 1
    else:
        all_freq[i] = 1
res = min(all_freq, key = all_freq.get) 
  
print (str(res))