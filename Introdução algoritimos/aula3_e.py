# Condicional de multipla escolha [ELIF]
'''
Exercicio 
Escreva um algoritmo em python em que o usuario escolhe se quer comprar maçãs, laranjas ou bananas. DEverá ser apresentado na tela 
um menu com as opções: 1 para maçã, 2 para laranja e 3 para banana

Após escolhida a fruta, deve-se digitar quantas unidades se quer comprar. O algoritimo deve calcular o preço total a pagar 
do produto ecolhido e mostrá-lo na tela

Considere que uma maçã custa R$ 2,30 uma laranja, R$ 3,60 e uma banana, R$ 1,85
'''
print('Escolha o que deseja ecolher:')
print('1 - Maçã')
print('2 - Laranja')
print('3 - Banana')
produto = int(input('Digite o numero correspondente a produto que você deseja: '))
qtd = int(input('Quandas unidades do produto deseja? '))

if (produto == 1 ):
    pagar = qtd * 2.3
    print(f'VocÊ compro {qtd} de maçãs. Total a pagar: {pagar:.2f}')
elif (produto == 2):
        pagar = qtd * 3.6
        print(f'VocÊ compro {qtd} de Laranjas. Total a pagar: {pagar:.2f}')
elif (produto == 3):
            pagar = qtd * 1.85       
            print(f'VocÊ compro {qtd} de Bananas. Total a pagar: {pagar:.2f}')
else:
    print('Produto não existe')