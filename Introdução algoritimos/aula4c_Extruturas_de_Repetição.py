#Estrutura de repetição FOR
'''
Assim como o whilr, essa estrtura repete um bloco de instruções enquanto a condição for verdadeira
No entanto, deferentemente do while, o for é empregado em situtações em que o numero
de vezes que o laço irá executar é finito e bem definido 
'''
for i in range(6):
    print(i)



for i in range(1,6,2): # (1,6,1) 1 = Valor inicial do iterador , 6 = valor final , 1 = passo do iterador
    print(i)

for i in range(10,0,-2): # Sentido decrescente 
    print(i)

# Podemos usar o For para fazer varreduras de string

frase = 'Lógica de programação e algorítimos'
for i in range (0, len(frase),1):
    print(frase[i], end="")
# Exercicio 
'''
Escreva um algoritmo que calcule a media dos numeros pares de 1 ate 100 ( 1 e 100 inclusos)
implemente usando o laço for
'''
soma = 0
qtd = 0
for i in range (1,101):
    if (i % 2 == 0):
        soma += 1
        qtd += 1
media = soma / qtd
print(f'A media dos pares de 0 ate 100 é: {media}')

#Estruturas de repetições aninhadas
'''
Podemos inserir laços dentro de outro laço
Não existe limite para quantos laços podemos colocar dentro de outro
Podemos misturar while e for 
'''
''' Escreva um algoritimo em python que calcule a tabuada de todos os numros de 1 até 10,e, para cada número
vamos calcular a tabuada multiplicando-o pelo intervalo de 1 até 10
'''
# 2 while
tabuada = 1 
while tabuada <= 10:
    print(f'TABUADA DO {tabuada}')
    i = 1
    while i <= 10:
        print(f'{tabuada} x {i} = {tabuada * i}') 
        i += 1
    tabuada +=1

# 2 for
tabuada = 1
for i in range (1,11,1):
    print(f'TABUADA DO {tabuada}')
    for i in range (1,11,1):
        print(f'{tabuada} x {i} = {tabuada * i}')

# while + for 
tabuada = 1
while tabuada <= 10:
    print(f'TABUADA DO {tabuada}')
    for i in range (1,11,1):
        print(f'{tabuada} x {i} = {tabuada * i}')
    tabuada += 1

'''
Vamos praticar exercícios envolvendo laços de repetição aninhados.

Exercício 1

Escreva um algoritmo que repetidamente pergunte ao usuário qual sua idade e seu sexo (M ou F). Para cada resposta o programa deve responder imprimir a mensagem:
“Boa noite, Senhor. Sua idade é <IDADE>” caso gênero masculino ou
“Boa noite, Senhora. Sua idade é <IDADE>” caso gênero feminino.
O programa deve encerrar quando o usuário digitar uma idade negativa.
'''

while True:
    print('Para sair, digite "-1"')
    
    idade = input('Digite a sua idade: ')
    if idade == "-1":
        print("Encerrando o programa...")
        break  # Encerra o loop caso o usuário digite "-1"
    
    # Converte idade para inteiro, garantindo que o usuário inseriu um número
    if idade.isdigit():
        idade = int(idade)
    else:
        print("Por favor, digite um número válido para idade.")
        continue

    genero = input('Informe seu gênero: M para masculino ou F para feminino: ').strip().upper()
    
    if genero == 'M':
        print(f'Boa noite, Senhor. Sua idade é {idade}')
    elif genero == 'F':
        print(f'Boa noite, Senhora. Sua idade é {idade}')
    elif genero not in ('M', 'F'):
        print('Digite um gênero válido')
