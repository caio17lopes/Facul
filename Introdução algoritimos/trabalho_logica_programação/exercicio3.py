'''
Enunciado: Você foi contratado para desenvolver um sistema de cobrança de serviços de uma copiadora. Você ficou com a parte de desenvolver a interface com o funcionário.
A copiadora opera da seguinte maneira:

•	Serviço de Digitalização (DIG) o custo por página é de um real e dez centavos;
•	Serviço de Impressão Colorida (ICO) o custo por página é de um real; 
•	Serviço de Impressão Preto e Branco (IPB) o custo por página é de quarenta centavos; 
•	Serviço de Fotocópia (FOT) o custo por página é de vinte centavos; 

•	Se número de páginas for menor que 20 retornar o número de página sem desconto;
•	Se número de páginas for igual ou maior que 20 e menor que 200 retornar o número de páginas com o desconto é de 15%;
•	Se número de páginas for igual ou maior que 200 e menor que 2000 retornar o número de páginas com o desconto é de 20%;
•	Se número de páginas for igual ou maior que 2000 e menor que 20000 retornar o número de páginas com o desconto é de 25%;
•	Se número de páginas for maior ou igual à 20000 não é aceito pedidos nessa quantidade de páginas;

♦	Para o adicional de encadernação simples (1) é cobrado um valor extra de 15 reais;
♦	Para o adicional de encadernação de capa dura (2) é cobrado um valor extra de 40 reais;
♦	Para o adicional de não querer mais nada (0) é cobrado um valor extra de 0 reais;

O valor final da conta é calculado da seguinte maneira:

total = (servico * num_pagina) + extra

'''
def borda (s1):
    tam = len(s1)# só imprime caso exista algum caractere
    if tam:
        print('+','-' * tam,'+')
        print('|',s1,'|')
        print('+','-' * tam,'+')

def escolha_serviço():
    opcao_valida = {'DIG','ICO','IPB','FOT'}
    preco = {
    'DIG':1.10,
    'ICO':1.00,
    'IPB':0.40,
    'FOT':0.20
    }
    while True:
        print('Selecione o serviço desejado: ')
        print('DIG - Digitalização → R$ 1.10 por página')
        print('ICO - Impressão colorida → R$ 1.00 por página')
        print('IPB - Impressão preta e branca → R$ 0.40 por página')
        print('FOT - Fotocópia → R$ 0.20 por página')
        print('Para encerrar digite sair')
        escolha = input("Digite a opção desejada: ").strip().upper()
        if escolha in opcao_valida:
            return escolha, preco[escolha]
        elif escolha == 'SAIR':
            print('Encerrando...')
            return None,0
        
        else:
            print('⚠ Opção invalida! Tente novamente...')
        print('\n')

def num_pagina():
    
    while True:
        try:
            qtd_pagina = int(input('Informe a quantidade de páginas que deseja para realizar o serviço: '))
            return qtd_pagina
        except ValueError:
            print('⚠ Opção invalida. Informe em numeral a quantidade de paginas que deseja!')

def serviço_extra():
    borda('Oferecemos serviços de encadernação:')
    extra = {
        'caderno_S': 15.00,
        'caderno_D': 40.00
    }
    while True:
        print('Encadernação capa simples : 15.00')
        print('Encadernação capa dura : 40.00')
        print('1 -Para encadernação capa simples ')
        print('2 - Para encadernação capa dura')
        print('0 - Sair')
        escolha = input('Digite a opção desejada: ')

        if escolha == '1':
            print(f'Serviço de encadernação simples selecionado: R$ {extra["caderno_S"]}')
            print('\n')
            return extra['caderno_S']
            
        elif escolha == '2':
            print(f'Serviço de encadernação capa dura selecionado: R$ {extra["caderno_D"]}')
            print('\n')
            return extra['caderno_D']
        elif escolha == '0':
            print('Nenhum serviço selecionado')
            return 0
        else:
            print('⚠ Opção inválida! Tente novamente.')
            print('\n')
            continue
        

def descontos (preco, pagina):

    while pagina > 20000:
        print('Não aceitamos pedidos maiores que 20000 páginas, faça o pedido novamente.')   
        pagina = num_pagina()
    
    total = preco * pagina
    desconto = 0
    
    if pagina <= 20:
        print(f'Seu pedido foi de {pagina}, seu desconto foi de R$ {desconto} ')
    elif  20 < pagina < 200:
        desconto = total * 0.15
        print(f'Seu pedido foi de {pagina},  seu desconto foi de R$ {desconto} ')
        print('\n')
    elif 200 < pagina < 2000:
        desconto = total * 0.20
        print(f'Seu pedido foi de {pagina},  seu desconto foi de R$ {desconto} ')
        print('\n')
    elif 2000 < pagina < 20000:
        desconto = total * 0.25
        print(f'Seu pedido foi de {pagina},  seu desconto foi de R$ {desconto} ')
        print('\n')
    return desconto 
    


#Programa Principal
qtd_serviço = 0
qtd_preco = 0

borda('Bem vindo a Copy do Caio Lopes!!!')
while True:
    servico, qtd_preco = escolha_serviço()
    if servico is None:
        break
    qtd_pagina = num_pagina()
    extra = serviço_extra()
    
    valor = (qtd_preco * qtd_pagina) + extra 
    desconto = descontos(qtd_preco, qtd_pagina)
    valor_final = valor - desconto

    qtd_serviço += 1 
    qtd_preco   += valor
    escolha = input('Se deseja mais um serviço digite S ou N para finalizar: ')
    if escolha != 'S':
        borda(f'Serviço pedido: {servico} . Quantidades de copias pedidas: {qtd_pagina} . Serviço extra {extra} . Valor total R$ {valor_final:.2f}  ')
        break
print('A Copy Caio Lopes agradece pelo seu pedido')
