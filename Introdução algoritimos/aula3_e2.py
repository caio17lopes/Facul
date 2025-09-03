#Exercicio 2
'''
Escreva um algortimo que leia um nome e uma idades
    Caso o nome digitado seja Vinicius, escreva isso na tela
    Caso o usuário digite qualquer outro nome, verifique sua idade. Se for menor que 18 anos, informe que é de menor. Se for de maior
    que 100 anos, informe que essa pessoa possivelmente não existe.

'''
nome = input('Informe seu nome: ').upper
idade = int(input('Qual a sua idade? '))

if (nome == 'Vinicius'):
    print(f'Olá Vinicius {nome}')
elif idade < 18:
    print('Você nã é o Vinicius. Você é menor de 18 anos!')
elif (idade > 18) and (idade < 99):
    print(f'Sua idade é {idade}')
elif idade > 100:
    print('Por acaso você andou no barro do diluvio?')
