# Criação de um programa que cadastra clientes para mecânica
# O cadsatro precisa ter:
# Propetário, modelo do carrro, fabricante, placa,ano do veiculo informação de reparo e valores gastos no veiculo 

# Programa principal 
banco_de_dados = {
    'cadastro': {
        'id': [],
        'proprietario': [],
        'veiculo': [],
        'fabricante': [],
        'ano_veiculo': [],
        'placa': [],
        'servico': [],
        'valor_pecas': [],
        'valor_servico': [],
        'data_servico': [],
        'observacao': []
    }
}

def borda(s1):
    tam = len(s1)
    if tam:
        print('+', '-' * tam, '+')
        print('|', s1, '|')
        print('+', '-' * tam, '+')

def cadastro():
    while True:
        id_cliente = len(banco_de_dados['cadastro']['id']) + 1  # Gera ID antes de adicionar os dados

        proprietario = input('Nome do proprietário: ').title()
        veiculo = input('Nome do veículo: ').upper()
        fabricante = input('Nome do fabricante: ').upper()
        ano_veiculo = input('Ano do veículo: ')
        placa = input('Placa do veículo: ').upper()
        servico = input('Informe o serviço efetuado: ')

        while True:
            try:
                valor_pecas = float(input('Valor das peças: '))
                break
            except ValueError:
                print("Erro! Digite um valor válido para as peças.")
        
        while True:
            try:
                valor_servico = float(input('Valor da mão de obra: '))
                break
            except ValueError:
                print("Erro! Digite um valor válido para o serviço.")

        data_servico = input('Data do serviço realizado: ')
        observacao = input('Adicione alguma observação se necessário: ')

        # Atualiza a lista de chaves antes de usar
        chaves = list(banco_de_dados['cadastro'].keys())

        # Adiciona os dados ao dicionário
        dados = [id_cliente, proprietario, veiculo, fabricante, ano_veiculo, placa, servico, valor_pecas, valor_servico, data_servico, observacao]
        for chave, valor in zip(chaves, dados):
            banco_de_dados['cadastro'][chave].append(valor)

        continuar = input('Deseja fazer mais um cadastro? (S/N): ').strip().upper()
        if continuar != 'S':
            break

def editar_cadastro():
    borda("Clientes Cadastrados")

    if len(banco_de_dados['cadastro']['id']) == 0:
        print("Nenhum cliente cadastrado.")
        return

    # Exibe todos os cadastros
    for i, dados in enumerate(zip(*[banco_de_dados['cadastro'][chave] for chave in chaves]), 1):
        print(f"{i}.")
        for chave, valor in zip(chaves, dados):
            print(f"{chave.replace('_', ' ').title()}: {valor}")
        print("=" * 40)

    # Solicita o número do cliente a ser editado
    try:
        indice = int(input('Escolha o número do cliente para editar (ou 0 para sair): ')) - 1
        if indice == -1:
            return  # Sai da função se o usuário escolher 0
        if indice < 0 or indice >= len(banco_de_dados['cadastro']['id']):
            print("Número inválido. Tente novamente.")
            return
    except ValueError:
        print("Opção inválida. Tente novamente.")
        return

    # Exibe o cliente escolhido
    cliente = {chaves[i]: banco_de_dados['cadastro'][chaves[i]][indice] for i in range(len(chaves))}
    print(f"Você escolheu editar o cliente: {cliente['proprietario']} ({cliente['veiculo']})")

    # Escolher qual campo editar
    campo = input("Digite o campo que deseja editar (exemplo: 'proprietario', 'veiculo', 'placa', etc.): ").strip().lower()

    if campo not in banco_de_dados['cadastro']:
        print("Campo inválido.")
        return

    # Edita o valor do campo escolhido
    novo_valor = input(f"Digite o novo valor para {campo.replace('_', ' ')}: ").strip()
    
    # Atualiza a informação no cadastro
    if campo == 'valor_pecas' or campo == 'valor_servico':
        try:
            novo_valor = float(novo_valor)  # Garante que o valor seja numérico
        except ValueError:
            print("Valor inválido. Deve ser um número.")
            return

    # Atualiza a lista
    banco_de_dados['cadastro'][campo][indice] = novo_valor
    print(f"{campo.replace('_', ' ').title()} foi atualizado com sucesso.")

# Função para exibir o menu e permitir edição
def menu():
    while True:
        print("\nMenu de Ações")
        print("1. Cadastrar cliente")
        print("2. Editar cliente")
        print("3. Exibir clientes")
        print("4. Sair")
        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            cadastro()
        elif escolha == '2':
            editar_cadastro()
        elif escolha == '3':
            borda("Clientes Cadastrados")
            for dados in zip(*[banco_de_dados['cadastro'][chave] for chave in chaves]):
                print("=" * 40)
                for chave, valor in zip(chaves, dados):
                    print(f"{chave.replace('_', ' ').title()}: {valor}")
                print("=" * 40, "\n")
        elif escolha == '4':
            break
        else:
            print("Opção inválida.")

menu()








