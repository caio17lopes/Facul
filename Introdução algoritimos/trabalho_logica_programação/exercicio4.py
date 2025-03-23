'''
Enunciado: Você e sua equipe de programadores foram contratados por pequena empresa para desenvolver o software de gerenciamento de livros. Este software deve ter o seguinte menu e opções: 
    Cadastrar Livro 
    Consultar Livro 
    Consultar Todos  
    Consultar por Id 
    Consultar por Autor 
    Retornar ao menu 
    Remover Livro 
    Encerrar Programa 
'''
def borda(s1):
    tam = len(s1)  # Só imprime caso exista algum caractere
    if tam:
        print('+', '-' * tam, '+')
        print('|', s1, '|')
        print('+', '-' * tam, '+')

def cadastrar_livro(id_global):
    global lista_livro  # Garante que estamos acessando a variável global
    # Criação do dicionário
    livro = {
        'id': id_global,  # Atribui o ID ao livro
        'nome': input('Digite o nome do livro: '),
        'autor': input('Digite o nome do autor: '),
        'editora': input('Digite o nome da editora: ')
    }
    lista_livro.append(livro)  # Adiciona o livro à lista
    id_global += 1  # Incrementa o ID para o próximo livro
    return id_global  # Retorna o novo ID

def consultar_livro():
    while True:
        borda('Escolha uma opção a seguir:')
        print('1 - Consultar todos: ')
        print('2 - Consultar por ID: ')
        print('3 - Consultar por autor:')
        print('4 - Voltar ao menu')

        escolha = input('Digite o número da opção: ')

        if escolha == '1':  # Consulta todos os livros
            if lista_livro:
                for livro in lista_livro:
                    print(f"ID: {livro['id']}, Nome: {livro['nome']}, Autor: {livro['autor']}, Editora: {livro['editora']}")
            else:
                print('Nenhum livro encontrado')

        elif escolha == '2':  # Consulta por ID
            try:
                id_procurado = int(input('Informe o ID do livro: '))
                encontrado = False
                for livro in lista_livro:
                    if livro['id'] == id_procurado:
                        print(f"ID: {livro['id']}, Nome: {livro['nome']}, Autor: {livro['autor']}, Editora: {livro['editora']}")
                        encontrado = True
                        break
                if not encontrado:
                    print('ID não encontrado')
            except ValueError:
                print('Digite um número valido')

        elif escolha == '3':  # Consulta por autor
            autor_procurado = input('Digite o nome do autor: ')
            encontrado = False
            for livro in lista_livro:
                if livro['autor'].lower() == autor_procurado.lower():
                    print(f"ID: {livro['id']}, Nome: {livro['nome']}, Autor: {livro['autor']}, Editora: {livro['editora']}")
                    encontrado = True
            if not encontrado:
                print(f'Nenhum livro encontrado para o autor "{autor_procurado}"')

        elif escolha == '4':  # Sai do loop e retorna ao menu
            break

        else:
            print('Opção inválida, tente novamente')

def remover_livro():
    global lista_livro  # Garante que estamos acessando a variável global
    try:    
        id_remover = int(input('Digite o ID do livro que deseja remover: '))
        encontrado = False
        for livro in lista_livro:
            if livro['id'] == id_remover:
                lista_livro.remove(livro)
                print(f'Livro com ID {id_remover} removido da lista de livros')
                encontrado = True
                break
        if not encontrado:
            print(f'ID {id_remover} não encontrado.')
    except ValueError:
        print('Digite um número valido')
# Programa principal
borda('Bem-vindo à Library Caio Lopes!')

lista_livro = []
id_global = 0

while True:
    borda('Escolha abaixo se deseja cadastrar, procurar ou deletar um livro ')
    print('1 - Cadastrar livro ')
    print('2 - Procurar um livro')
    print('3 - Remover um livro')
    print('4 - Sair')

    escolha = input('Informe o número da opção que deseja: ')
    
    if escolha == '1':
        id_global = cadastrar_livro(id_global)  # Atualiza id_global corretamente
    elif escolha == '2':
        consultar_livro()
    elif escolha == '3':
        remover_livro()
    elif escolha == '4':
        print("Saindo do sistema...")
        break
    else:
        print("Opção inválida! Tente novamente.")
