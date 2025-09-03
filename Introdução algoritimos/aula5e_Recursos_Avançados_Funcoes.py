# Recursos avançados em funções
'''
Erro de sintaxe:
Ocorre quando o programador comete algum erro de digitação, ou esquece de alguma palavra chave, ou caractere, ou mesmo
erra na identação do código 
'''
# Erro sintaxe
while True: # sem os dois pontos, so coloquei para tirar o erro
    print('Olá mundo')
    break

#Exceção
'''
Neste tipo de erro, a sintaxe está correta, porém um erro durante a execução do programa ocorre,
normalmente devido a um dado digitado de maneira inválida e não tratado durante o programa
'''
# Exceções comuns em python
'''
ZeroDivisionError - erro de divisão por zero
ValueErro - erro de uma dado não esperado digitado
IndexError - erro de indice inexistente sendo acessado
'''
print(100 * (2/0))
x = int(input('Por favos digite um número: '))


# Uso except

while True:
    try:
        x = int(input('Por favos digite um número: '))
        break
    except ValueError:
        print('Oops! Número invalido. Tente novamente....')

i = 0
while True:
    try:
        nome = input('Por favor digite seu nome: ')
        ind = int(input('Digite um indice do seu nome digitado'))
        print(nome[ind])
        break
    except ValueError:
        print('Oops! Nome invalido. Tente novamente....')
    except IndexError:
        print('Oops! Indice invalido. Tente novamente....')
    finally:
        print(f'Tentativa{i}')
        i += 1

def div():
    try:
        num1 = int(input('Digite um número'))
        num2 = int(input('Digite um número'))
        res = num1 / num2
    except ZeroDivisionError:
        print('Erro de divisão por zero')
    except:
        print('Algo aconteceu...')
    else:
        return res
    finally:
        print('Executara sempre')

print (div())

