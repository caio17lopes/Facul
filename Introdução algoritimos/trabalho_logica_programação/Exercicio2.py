def calcular_pagamento(qtd_horas, valor_hora):
    horas = float(qtd_horas)
    taxa = float(valor_hora)
    if horas <= 40:
        salario=horas*taxa
    else:
        h_excd = horas - 40
        salario = 40*taxa+(h_excd*(1.5*taxa))
    return salario

str_horas= input('Digite as horas: ')
str_taxa=input('Digite a taxa: ')
total_salario = calcular_pagamento(str_horas,str_taxa)
print('O valor de seus rendimentos é R$',total_salario)

def velhice(nome,idade):
    nomes = str(nome)
    anos = int(idade)
    if anos <= 35:
        print(f'Você é jovem {anos}')
    elif anos >= 36 or anos <= 59:
        print(f'Você é um coroa {anos}')
    else:
        print(f'Você é idoso {anos}')
    return nomes,anos

seu_nome = input('digite seu nome: ')
idade = int(input('Digite sua idade'))
print('Seu nome é: ', velhice(seu_nome), 'e sua idade é: ', velhice(idade) )