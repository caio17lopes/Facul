'''
Escreva um algoritmo que leia dois valores numéricos e que pergunte ao usuário qual operação ele deseja realizar: 
adição (+), subtração (-), multiplicação (*) ou divisão (/). Exiba na tela o resultado da operação desejada.
'''
print(' CALCULADORA')
print('Selecione a seguir o tipo de operação que deseja fazer:')
print('+ ADIÇÃO')
print('- SUBTRAÇÃO')
print('* MULTIPLICAÇÃO')
print('/ DIVISÃO')
print('APERTE QUALQUER OUTRA TECLA PARA SAIR')

op = input('Qual operação deseja realizar? ')
x = int(input('Digite o primeiro número: '))
y = int(input('Digite o segundo número: '))

if (op == '+'):
    res = x + y
    print(f'O resultado de {x} + {y} = {res}')
elif (op == '-'):
    res = x - y
    print(f'O resultado de {x} - {y} = {res}')
elif (op == '*'):
    res = x * y
    print(f'O resultado de {x} * {y} = {res}')
elif (op == '/'):
    res = x / y
    print(f'O resultado de {x} / {y} = {res}')
else:
    print('OPERAÇÃO INVALIDA!')