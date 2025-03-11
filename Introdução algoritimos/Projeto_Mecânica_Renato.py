# Criação de um programa que cadastra clientes para mecânica
# O cadsatro precisa ter:
# Propetário, modelo do carrro, fabricante, placa,ano do veiculo informação de reparo e valores gastos no veiculo 

# Programa principal 
banco_de_dados= {
    'cadastro': {
        'proprietario':[],
        'fabricante':[],
        'veiculo': [],
        'ano_veiculo':[],
        'placa': [],
        'serviço': [],
        'valor_pecas':[],
        'valor_serviço': [],
        'data_serviço':[],
        'observação':[]
    }
}

def cadastro():
    while True:
        proprietario = input('Nome do proprietário: ').title()
        fabricante = input('Nome do fabricante: ').upper()
        veiculo = input('Nome do veiculo: ').upper()
        ano_veiculo = input('Ano do veiculo: ')
        placa = input('Placa do veiculo: ').upper()
        servico = input('Informe o serviço efetuado: ')

        while True:
            try:
                valor_peças = float(input('Valor das peças: '))
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
        #Adiciona as informações no vanco de dados
        banco_de_dados['cadastro']['proprietario'].append(proprietario)
        banco_de_dados['cadastro']['fabricante'].append(fabricante)
        banco_de_dados['cadastro']['veiculo'].append(veiculo)
        banco_de_dados['cadastro']['ano_veiculo'].append(ano_veiculo)
        banco_de_dados['cadastro']['placa'].append(placa)
        banco_de_dados['cadastro']['servico'].append(servico)
        banco_de_dados['cadastro']['valor_peças'].append(valor_peças)
        banco_de_dados['cadastro']['valor_servico'].append(valor_servico)
        banco_de_dados['cadastro']['data_servico'].append(data_servico)
        banco_de_dados['cadastro']['observacao'].append(observacao)
        
        
cadastro()
print('Clientes cadastrados: ')



