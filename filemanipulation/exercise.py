alunos = {'Pedro' : 8.0,
          'Maria': 10.0,
          'Amilton': 7.5}

carros = {'Hyundai' : 'Creta',
          'Nissan': 'Kicks',
          'Volkwagen': 'Tiguan'
          }

with open('filemanipulation/notas.txt','w') as nt:
    for aluno, nota in alunos.items():
        nt.writelines(f'{aluno} : {nota}\n')

with open('filemanipulation/carros.txt','w') as cars:
    for marca, modelo in carros.items():
        cars.write(f' Marca: {marca} | Modelo: {modelo} \n')

with open('filemanipulation/notas.txt') as rcar:
    for linha in rcar:
        print(linha)

with open('filemanipulation/carros.txt') as rcar:
    for linha in rcar:
        print(linha)

    