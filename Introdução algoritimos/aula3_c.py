#Exercicios
# Desenvolva um algoritimo que solicite seu an ode nascimento e o ano aual para calcular sua idade e a presente na tela

ano_nasc =int(input('Digite o ano de seu nascimento: '))
ano_atual =int(input('Digite o ano que você esta: '))
idade = ano_atual - ano_nasc
print(f'Sua idade atual é de:{idade}')
if (idade >= 18):
    print('Você é de maior idade e ja pode dirigir')
else:
    ('Você é de menor')
'''
Uma empresa concedeu um bônus de 20% para todos seus funcionários com mais de cinco anos de empresa. 
Todos os outros que não se enquadram nesta categoria receberam uma bonificação de 10%, somente. 
Escreva um algoritmo que leia o salário do funcionário e seu tempo de empresa, e apresente a bonificação de cada funcionário na tela.

'''
tempo_casa = int(input('Digite quanto tempo de casa você tem: '))
salario = float(input('Informe seu salario: '))
if (tempo_casa >5):
    bonus = salario * 0.2
else:
    bonus = salario * 0.1
print(f'Seu tempo de empresa é de {tempo_casa}')
print(f'Seu salário é de {salario:.2f}')
print(f'E sua bonificação é de {bonus:.2f}')
print(f'Seu salario total foi de {bonus + salario:.2f}')

