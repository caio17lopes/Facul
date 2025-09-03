# Parâmetros de funções
# Definição 
'''
Parâmetros: dados recebidos pelas funções
O ato de enviar um dado para uma função é chamdo de passagem de parâmetro
'''
def realce (s1):
    print('|', '__' *10,'|')
    print('|', '__' *10,'|')
    print(s1)
    print('|', '__' *10,'|')        
    print('|', '__' *10,'|')

# Programa principal
realce('          MENU')

def sub2(x,y):
    res = x - y
    print(res)
sub2(5,7)

#Parâmetros opicionais
'''Podemos dar maior flexibidade para nossas funções permitindo que nem sempre se use 
todos os parâmetros na chamada função

''' 
def soma3 (x, y, z):
    res = x + y + z
    print(res)

def soma3 (x = 0, y = 0, z = 0): # Colocando zero indica um valor padrão da variavel, nos omitimos  a variavel podendo usar apenas 2 ou 1.
    res = x + y + z
    print(res)
soma3 (1,2,3) 
soma3(1,2) # Z foi omitido
soma3(1) # Y e Z foram omitidos
soma3() # Todos foram omitidos

#Exercicio 

'''
Escreva uma rotina que crie uma borda ao redor de uma palvra, para destacá-la como sendo titulo. Aorotina deve receber como parâmetro a palavra a ser destacada. 
O tamanho da caixa de terxto deverá ser adaptável, de acord com o tamnho da palvara. 
'''
def borda (s1):
    tam = len(s1)
    # só imprime caso exista algum caractere
    if tam:
        print('+','-' * tam,'+')
        print('|',s1,'|')
        print('+','-' * tam,'+')
    
borda (input('Digite um texto aqui: '))
borda (input('Digite outro texto aqui: '))
# Outro mode de fazer a cima:
'''
borda ('Olá mundo ')
borda ('Logica de programação e algoritimos')
'''
