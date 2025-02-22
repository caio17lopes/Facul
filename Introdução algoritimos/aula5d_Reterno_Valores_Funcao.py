# Retrono de valores em funções

# Função x Procedimento
'''
Procedimento (procedure) - uma rotina sem retorno
Função - uma rotina que retorna um dado a quem invocou 
'''
def soma3 ( x = 0, y = 0, z = 0):
    res = x + y + z
    return res # Estou retornando a variavel res paraa o programa principal
# Programa principal
retornado = soma3 (1,2,3)
print(retornado)
# Forma alternativa simplificada
print(soma3(2,2))

#programa principal

retornado1 = soma3(1,2,3)
retornado2 = soma3(1,2)
retornado3 = soma3()
print(f'Somatórias: {retornado1}, {retornado2} e {retornado3}.')
#Exercicio 
def valida_string(pergunta, min, max):
    s1 = input(pergunta)
    tam = len(s1)
    while (( tam < min) or ( tam > max)):
        s1 = input (pergunta)
        tam = len(s1)
    return s1
# programa principal
x = valida_string('Digite uma string: ', 10,30)
print('Você digitou a string: {}. \nDado válido. Encerrando o programa...'.format(x))