'''
Enunciado: Você e sua equipe de programadores foram contratados para desenvolver um app de vendas para uma loja que vende Açaí e Cupuaçu. 
Você ficou com a parte de desenvolver a interface do cliente para retirada do produto.
A Loja possui seguinte relação:

•	Tamanho P de Cupuaçu (CP) custa 9 reais e o Açaí (AC) custa 11 reais;
•	Tamanho M de Cupuaçu (CP) custa 14 reais e o Açaí (AC) custa 16 reais;
•	Tamanho G de Cupuaçu (CP) custa 18 reais e o Açaí (AC) custa 20 reais;
'''
def borda (s1):
    tam = len(s1)# só imprime caso exista algum caractere
    if tam:
        print('+','-' * tam,'+')
        print('|',s1,'|')
        print('+','-' * tam,'+')

def menu():
    borda('Bem vindo a Sorveteria Caio Lopes!')
    borda('''Tamanhos    Cupuaçu       Açai
    P    |    R$ 9.00   |   R$ 11.00
    M    |    R$ 14.00  |   R$ 16.00
    G    |    R$ 18.00  |   R$ 20.00 
''')
def valor ():
    precos = {
        'CP': {'P':9, 'M':14, 'G':18},
        'AC':{'P':11, 'M':16, 'G':20}
    }
    total = 0 # soma a quantidade de pedidos
    while True:
        produto = input('Digite "CP" para Cupuaçu ou "AC" para Açai: ').upper()
        if produto != 'CP' and produto != 'AC':
            print('Digite um sabor valido! "CP" para Cupuaçu ou "CA" para Açai')
            continue # volta para o inicio do loop ate a pessoa preeencher o valor de forma correta
        tamanho = input('Digite o tamnho desejado, "P" para pequeno, "M" para medio ou "G" para grande:  ').upper()
        if tamanho != 'P' and tamanho != 'M' and tamanho != 'G':
            print('Digite um tamanho valido! "P" para pequeno, "M" para medio ou "G" para grande')
            continue # volta para o inicio do loop ate a pessoa preeencher o valor de forma correta
        total += precos[produto][tamanho] # ele acumula o valor do pedido pelo tamanho e o valor seguindo o dicionario
        sair = input('Você deseja fazer mais algum pedido? Digite "S" para fazer mais pedidos ou "N" para encerrar: ').upper()
        if sair == 'N':
            break # encerra todo o loop 
        else:
            continue # volta no inicio do loop caso o cliente queira fazer mais um pedido
    return total # retorna o valor da operação

#Programa principal
menu()

preco = valor() # preco recebe o resultado da função valor 
borda(f'O valor a ser pago é R$ {preco:.2f}') # entrega o valor final para o cliente