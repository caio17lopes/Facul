'''
Faça um algoritimo que recebe três valores, representando os lados de u mtriangulo fornecido pelo usuario.
Verifique se os valores forman um triangulo e classifique como:
a) Equilatero
b) Isosceles
c) Escaleno
'''
A = int(input('Digite o 1° lado do triângulo: '))
B = int(input('Digite o 2° lado do triângulo: '))
C = int(input('Digite o 3° lado do triângulo: '))

if ((A > 0 and B > 0 and C > 0) and (A + B > C and B + C > A and A + C > B )):
    # se chegou ate aqui deu bom
    if ( A != B and B != C and A != C):
        print('Esse é um traingulo escaleno')
    else:
        if ( A == B and B == C and A == C):
            print('Esse é um triângulo equilatero')
        else:
            print('Esse é um triangulo isosceles')
else:
    print('Ao menos um dos valores indicados não serve para formar um triangulo')

########################################################################################################################

# Calculo de kwh e dando valor

kwh = float(input('Informe quantos KWH você gastou'))
tipo = input(' Informe qual o tipo de instalação eletrica : R ou I e C ')

if ( tipo == 'R'):
    if  kwh >= 500 :
        preco = 0.65
        total = kwh * preco
    else:
        preco = 0.55
        print(f'Total a pagar : {kwh * preco}')
elif( tipo == 'I'):
    if  kwh >= 1000 :
        preco = 0.60
        total = kwh * preco
    else:
        preco = 0.55
        print(f'Total a pagar : {kwh * preco}')

elif( tipo == 'C'):
    if  kwh >= 1000 :
        preco = 0.60
        total = kwh * preco
    else:
        preco = 0.55
        print(f'Total a pagar : {kwh * preco}')

else: 
    print('Instalção invalida!')
