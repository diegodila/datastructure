#function to extract CEP, URL, NUMBERS
import re


pysites = ['http://www.pyregex.com/', 'https://regex101.com/', 'https://pyladies.com/', 'https://brasil.pyladies.com/']

numbers = ['diego:55+11-92002-2221 - lorem ipsum','brook:65+11-920022221 - lorem', 'vreo:05+11-92002-2221 - sope ipsum','kdse:43+1192002-2221 - lorem ipsum alburw' ]

ceps = ['diego CEP:02042-010http://www.pyregex.com/', 'https://regexdiego CEP:02042-010-101.com/', 'htdiego CEP:02042-010tps://pyladies.com/', 'https:/diego CEP:02042-010/brasil.pyladies.com/']

    
with open('regularexpressions/extractsites.txt', 'w') as txt:
    for site in pysites:
        aux = re.findall('\w+\:\W*\w*\.\w+\W*\w*\W*', site)
        txt.writelines(f'{aux}\n')

with open('regularexpressions/extractnumbers.txt', 'w') as txt:
    for number in numbers:
        aux = re.findall('\d{2}\W\d{2}\W*\d{4,5}\W*\d{4}', number)
        txt.writelines(f'{aux}\n')

with open('regularexpressions/extractceps.txt', 'w') as txt:
    for number in ceps:
        aux = re.findall('\w{3}\W*\d{5}\W*\d{3}', number)
        txt.writelines(f'{aux}\n')