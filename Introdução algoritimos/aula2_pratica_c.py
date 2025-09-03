'''
Exercicio 3

Crie uma variavel de string que receba uma frase qualquer. 
Crie uma segunda variavel, agora contendo a metade da sting digitada.
Imprima na tela somente os odis ultimos caracteres da segunda variavel do tipo string

'''

frase = input('Digite uma frase: ')
tam = len(frase)

frase2 = frase [:int(tam/2)]

print(frase[-2:])