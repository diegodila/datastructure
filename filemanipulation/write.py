with open('filemanipulation/texto.txt','w') as tx:
    tx.write('Teste de escrita')

with open('filemanipulation/texto1.txt','w') as tx1:
    tx1.writelines('teste de multiplas linhas')