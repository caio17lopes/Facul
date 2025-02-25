# Docstring
'''
Strings inserids entro de nosso codigo python que explicam o funcionamento dele
A string é colocada na primeira linha de cadad definição
Isso já é o que eu ja faço
'''
#Exercicio 1

def soma3 ( x = 0, y = 0, z =0):
    
    '''
    So escrevendo qualquer coisa para aparecer no print

    '''
    return  x + y + z
print(soma3(1,2,3))
help(soma3)

#Exercicio 2
def fatorial (num):

    fat = 1
    if num == 0:
        return fat
    # esta parte só executa caso num > 0 
    for i in range (1, num + 1,1):
        fat *= i
    return fat 

x = int(input('Digite um valor para calcular a fatorial: '))
print(f'{x}! = {fatorial(x)}')


# Exercicio 3 crie uma função para cada item 

def valida_int(pergunta, min, max):
    while True:
        try:
            x = int(input(pergunta))
            if min <= x <= max:
                return x
            else:
                print(f"Erro: Digite um número entre {min} e {max}.")
        except ValueError:
            print("Erro: Digite um número inteiro válido.")


def existeArquivo(nomeArquivo):
    try:
        a = open(nomeArquivo, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True
    
def criarArquivo(nomeArquivo):
    try:
        a = open(nomeArquivo, 'wt+')
        a.close()
    except:
        print('Erro na criação do arquivo')
    else:
        print(f'Arquivo {nomeArquivo} criado com sucesso')

def cadastrarJogo(nomeArquivo, nomeJogo, nomeVideogame):
    try:
        a = open(nomeArquivo, 'at')
    except:
        print('Erro ao abrir o arquivo....')
    else:
        a.write(f'{nomeJogo};{nomeVideogame}\n')
    finally:
        a.close()

def listarArquivo(nomeArquivo):
    try:
        a = open(nomeArquivo, 'rt')
    except:
        print('Erro ao ler o arquivo...')
    else:
        print(a.read())
    finally:
        a.close()
# Programa principal



arquivo = 'games.txt'
if existeArquivo(arquivo):
    print('Arquivo localizado no computador')

else:
    print('Arquivo inexistente')
    criarArquivo(arquivo)

while True:
    print('Menu')
    print('1 - Cadastrar novo item')
    print('2 - Listar cadastros')
    print('3 - sair')

    op = valida_int ('Escolha a opção desejada: ',1,3)
    if (op == 1):
        print('Opção de cadastrar novo item selecionada...')
        nomeJogo = input('Nome do jogo: ')
        nomeVideogame = input('Nome do videogame: ')
        cadastrarJogo(arquivo,nomeJogo,nomeVideogame)
    elif (op == 2):
        print('Opção listar selecionada...')
        listarArquivo(arquivo)
    elif (op == 3):
        print('Encerrando o programa.....')
        break