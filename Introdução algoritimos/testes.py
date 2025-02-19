total = 0
dinheiro = 0 
while True:
    idade = int(input('Qual a sua idade? '))
    if idade == 0 :
        break                 
    total += 1  
    if idade <3:  
        ingresso = 0
    else:
        if idade > 12 :
        ingresso = 30
        else:
        ingresso = 15
    dinheiro += ingresso

if total >0:
    media = idade / total
    print(f'Total de pessoas: {total}')
    print(f'Total arrecadado: {dinheiro}')
    print(f'Media arrecadada: {media}')