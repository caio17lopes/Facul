# TÓPICOS IMPORTANTES COM LAÇOS EM PYTHON

soma = 0
cont = 1
while (cont <= 5):
    x = int(input(f'Digite o {cont}ª numero: '))
    soma += x # Equivalente : soma = soma + x
    cont += 1 # Equivalente : cont = cont + 1
print(f'Somatoria {soma}')

# VALIDANDO ENTRADAS COM UM LOOP

x = int(input('Digite um valor maior que zero: '))
while (x <= 0):
    x = int(input('Digite um valor maior que zero: '))
print(f'Você digitou {x}, encerrando o programa...')

# INSTRUÇÃO BREAK 

print('Digite uma mensagem que eu irei repetir para você!')
print('Digite sair para parar')
while True:
    texto = input('')
    if texto == 'sair':
        break
print('encerrando programa')

# Comando continue serve para retornar o laço ao inicio

while True:
    nome = input('Qual o seu nome: ')
    nome = nome.title()
    if (nome  != 'Caio'):
        print('Nome de usuario incorreto')
        continue # Volta ao inicio caso o nme seja errado
    senha = input('Qual a sua senha')
    if (senha != 'azaradao18'):
        print('Senha invalida')
        continue
    break # encerra todo o laço 
print('Acesso permitido')

# Valores Truthy e Falsey
'''
São usados para dados não booleanos, podem ser tratados como True e False
Falsey / FAlse
    Numero zero ( int ou float ) e string vazia

Truthy / True
    Qualquer outro dado
'''
nome = ''
while not nome : 
    # encerra o laço quado nome não estive vazio
    nome = input('Digite seu nome: ')
valor = int(input('Digite um número qualquer'))
if valor: # equivale a if valor !=0
    print('Você digitou um valor difrente de zero')
else:
    print('Você digitou zero')
