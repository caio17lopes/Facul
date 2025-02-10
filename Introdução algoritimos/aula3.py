# Algoritimos Sequenciais 

# Condicional simples e compostas 
'''
Exercicio 
Desenvlva um programa que leia dois valores numéricos inteiros e compare se o 
primeiro é maior do que o segundo,
utilizando uma condicional simples

Caso seja (resultado verdadeiro), ele imprime na tela a mensagem informando que o primeiro
valor digitado é maior do que o segundo
'''
# Lê dois valores e compara ambos
x = int(input('Digite um valor inteiro: '))
y = int(input('Digite um segundo valor inteiro: '))
if (x>y):
    print('O primeiro valor é maior que o segundo!')


# Lê dois valores inteiros e compara ambos e retorna as duas condições
x = int(input('Digite um valor inteiro: '))
y = int(input('Digite um segundo valor inteiro: '))
if (x>y):
    print('O primeiro valor é maior que o segundo!')
if (x<y):
    print('O segundo valor é maior que o primeiro!')

# Condicional do tipo composta
x = int(input('Digite um valor inteiro: '))
y = int(input('Digite um segundo valor inteiro: '))
if (x>y):
    print('O primeiro valor é maior que o segundo!')
else:
    print('O segundo valor é maior que o primeiro!')
    
# Desenvolva um programa que leia um valor inteiro e descubra se ele é par ou impar

x = int(input('Digite um numero inteiro'))
if(x % 2 == 0):
    print(' O numero é par!')
else:
    print('Esse numero é impar!')