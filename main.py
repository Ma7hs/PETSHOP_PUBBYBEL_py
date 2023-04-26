import time

count = 1

print('BEM VINDO A PETSHOP PUBBYBEL')
print('A PARTIR DE AGORA TEREMOS INICIO NA NOSSA CAMPANHA DE VACINAÇÃO')
print('===================================================================')

while True:
    especie = input('Qual é a espécie do animal? ')
    nome = input(f'Qual é o nome do {especie}? ')

    listOfVacine = [
        'Giardiase',
        'Raiva',
        'V8'
        ]
    for i in listOfVacine:
        print(f'A vacina {i} foi aplicada com sucesso')
        time.sleep(2)

    print(f'''
     Espécie: {especie},
     Nome: {nome}, 
     Número: {count} \n''')

    resposta = input('Tem mais um animal? Responda com 1 = SIM ou 0 = NÃO: ')
    print('===================================================================')
        
    while resposta != '0' and resposta != '1':
        print('Resposta inserida de maneira incorreta!')
        resposta = input('Digite 1 para SIM e 0 para NÃO:')
        print('===================================================================')
   
    if resposta == '0':
        break
    elif resposta == '1':
      count += 1
      
if count == 1:
  print(f'Apenas o animal de número {count} foi vacinado')
elif count >=2:
  print(f'Foram vacinados um total de {count} animais')  
