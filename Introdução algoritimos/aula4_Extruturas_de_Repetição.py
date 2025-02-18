# Estrutura de repetição 
'''
while (enquanto)
for (para)
Laços de repetições aninhados
'''
# While (enquanto)
# Repete um bloco enquanto a condição for verdadeira, se for falso ele sai do laço

x = 1
while ( x <= 5):
    print(x)
    x = x + 1

x = 0 
while (x <= 99):
    print(x)
    x = x +1

x = 0 
while (x < 100):
    print(x)
    x = x +1

# Exercicio com contador 
'''
Escreva um algoritimo que imprima na tela somente valores dentro de um intervalo especificado
pelo usuario e que sejam numeros pares
'''
inicial = int(input('Qual valor deseja iniciar a contagem? '))
final = int(input('Qual valor deseja encerrar a contagem? '))
x = inicial
while (x <= final):
    # Verificar se o numero é par
    if ( x % 2 == 0):
        print(x)
    x = x + 1

# Exercicio com acumulador
'''
Escreva um algoritimo que calcule a sua media de notas em determinada disciplina
Vamos assumir que a media final é dada pela media a ritmetica de cinco notas digitadas
'''

soma = 0 
cont = 1 
while (cont <= 5):
    x = float(input(f'Digite a {cont}ª nota: '))
    soma = soma + x
    cont = cont + 1
media = soma / 5
print(f'MEdia final : {media}')
