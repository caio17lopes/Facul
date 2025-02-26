def borda (texto):
    tam = len(texto)
    
    if tam:
        print('+','-' * (tam ),'+')
        print('|',texto,'|')
        print('+','-' * (tam ),'+')

def menu ():
    
    while True:
        try:
            print('')
            print('Escolha uma das opções a seguir de pratos:\n')
            print('1 - Menu 1')
            print('2 - Menu 2')
            print('3 - Menu 3')
            print('4 - Sair')
            
            
            op = int(input('Digite a opção para ver as opções de menu: '))
            if op == 1:
                borda ('Menu 1 escolhido')
                menu1(1,)
            elif op == 2:
                borda ('Menu 2 escolhido')
                menu2(1)
            elif op == 3:
                borda ('Menu 3 escolhido')
                menu3(1)
            elif op == 4:
                print('Encerrando o menu...')
                
                break
            else:
                print(f'Digite um da opções a cima:')
        except ValueError:
            print('Opção invalida, tente novamente por favor.')

def menu1 (card,valor):
    print('Opção 1 -')
    print('Entrada = Gravelax de salmão na brusqueta com azeite de trufa')
    print('Prato Principal = Terrine de Salmão com caviar e trufa ')
    print('Sobremesa = Sorbe de acerola com morango, com uma deliciosa calda de chocolate')
    print('-'*45)
    valor = 145.00
    valor1 = int(valor)
    return valor1, card

def menu2 (valor2):
    print('Opção 2 -')
    print('Entrada = Carpacio de contra filé')
    print('Prato Principal = Filé ao molho poavire e fritas ')
    print('Sobremesa = Parfait de chocolate e morango')
    print('-'*45)
    valor = 105.00
    valor2 = int(valor)
    return valor2

def menu3 (valor3):
    print('Opção 3 -')
    print('Entrada = Aneis de lula')
    print('Prato Principal = Panelada dos marés')
    print('Sobremesa = Salada de fruta dos reis')
    print('-'*45)
    valor = 119.00
    valor3 = int(valor)
    return valor3

#def quantidade (qtd):
 #   while True:

borda('Bem vindo ao restaurante MasterChef!')
menu()



# Preciso coloca valores nos pratos, bebidas e quantidade consumida para dar o valor total ao cliente