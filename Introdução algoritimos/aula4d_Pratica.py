'''
while x for
Realize a sequência de print com for e while
a) Inteiros de 3 até 12, com 12 incluso 
b) Interios de 0 ate 9, excluindo 9 com passo de 2
'''
i = 3
while i <=12:
    print(f'Cntando... {i}')
    i += 1
print('-------------------')
i = 0
for i in range(3,13):
    print(f'Contando... {i}')
print('-------------------')
#b) Interios de 0 ate 9, excluindo 9 com passo de 2

i = 0 
while i <=9:
    print(f'Contando... {i}')
    i += 2
print('-------------------')

i = 0
for i in range(0,9,2):
    print(f'Contando... {i}')

print('-------------------')

# Exercicio 
'''
Escreva um algoritimo que mostra, na tela, quatro produtos a serem comprados em uma lanchonete:
Coxinha - R$ 5,00
Patel - R$ 7,00
Café - R$ 4,00
Suco - R$ 6,00
Faça um algoritimo em que você seleciona o produto que quer e a quantidade 
Faça isso ate que decida encerrar o programa 
Ao final mostre o valor final do produto
'''
print('LANCHONETE')
print('####################')
print('1 - Coxinha R$ 5,00')
print('2 - Pastel R$ 7,00')
print('3 - Café R$ 4,00')
print('4 - Suco R$ 6,00')
print('5 - Sair')

total = 0
while True:
    op = int(input('Qual item gostaria de comprar? '))

    if (op == 1):
        qtd = int(input('Quantas unidades deseja comprar? '))
        total = total + qtd * 5.00
    elif (op == 2):
        qtd = int(input('Quantas unidades deseja comprar? '))
        total = total + qtd * 7.00
    elif (op == 3):
        qtd = int(input('Quantas unidades deseja comprar? '))
        total = total + qtd * 4.00
    elif (op == 4):
        qtd = int(input('Quantas unidades deseja comprar? '))
        total = total + qtd * 6.00
    elif (op == 5):    
        break
    else:
        print('Produto invalido. Selecione outro')

print(f'\nO total a ser pago R$ {total:.2f}')

''' Escreva um algortitimo que leia um valor e que imprima a quantidade de cedulas
necessarias para pagar esse mesmo valor. Para simplificar vamos trbalhar apenas com
valores inteiros e com cedulas de 100, 50, 20, 10, 5, 1.

'''
print('Caixa do Robertão')
valor = int(input('Informe quanto de dinheiro você precisa retirar: R$ '))

while True:
    if valor >= 100:
        cont100 = valor // 100
        valor = valor - cont100 * 100
        print(f'Cédulas de 100: {cont100}')
        if not valor:
            break

    if valor >= 50:
        cont50 = valor // 50
        valor = valor - cont50 * 50
        print(f'Cédulas de 50: {cont50}') 
        if not valor:
            break     
    
    if valor >= 20:
        cont20 = valor // 20
        valor = valor - cont20 * 20
        print(f'Cédulas de 20: {cont20}')
        if not valor:
            break

    if valor >= 10:
        cont10 = valor // 10
        valor = valor - cont10 * 10
        print(f'Cédulas de 10: {cont10}')
        if not valor:
            break

    if valor >= 5:
        cont5 = valor // 5
        valor = valor - cont5 * 5
        print(f'Cédulas de 5: {cont5}')
        if not valor:
            break

    if valor:
        cont1 = valor
        print(f'Cédulas de 1: {cont1}')
        break

##################################################################
total = 0
dinheiro = 0 
acc_idade = 0
while True:
    idade = int(input('Qual a sua idade? '))
    if idade == 0 :
        break                 
    total += 1
    acc_idade += idade
    if idade <3:  
        ingresso = 0
    else:
        if idade > 12 :
            ingresso = 30
        else:
            ingresso = 15
    dinheiro += ingresso

if total >0:
    media = acc_idade / total
    print(f'Total de pessoas: {total}')
    print(f'Total arrecadado: {dinheiro}')
    print(f'Media arrecadada: {media}')