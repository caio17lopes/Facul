# String e listas dentro de listas
mochila = ('Machado', 'Camisa', 'Bacon', 'Abacate')
#mochila [0][0]  Entrei na lista e depois entrei dentro da string
print(mochila[0][0])
print(mochila[2][1])

for item in mochila:
    for letra in item:
        print(letra, end='')
    print()

mochila = ('Machado', 'Camisa', 'Bacon', 'Abacate')
for i in range(0,len(mochila),1):
    for j in range(0,len(mochila[i]),1):
        print(mochila[i][j],end='')
    print

# Listas dentro de Listas
mochila = [['Cebola',0.39],['Tomate',0.49],['Maçã', 0.89]]
print(mochila[0][1])

# Imagine uma situação na qual você deve realizar o cadastro de uma lista de compras em um sitema. Cada produto comprado deverá ser
# registrado com seu nome, quantidade e valor unitario 

item = []
mercado = []

for i in range(3):
    item.append(input('Digite o nome do item: '))
    item.append(int('Digite a quantidade: '))
    item.append(float('Digite o valor: '))
    mercado.append(item[:])
    item.clear()
print(mercado)

# Mesmo exercicio de cima só que de forma mais facil

mercado = []
for i in range(3):
    nome = input('Digite o nome do item: ')
    qtd = int(input('Digite a quantidade'))
    valor = float(input('Digite o valor'))
    mercado.append([nome,qtd,valor])
print(mercado)

# Adicional de soma da lista:

soma = 0 
print('Lista de compras: ')
print('-'*20)
print('item | quantidade | valor unitário | total do item')
for item in mercado:
    print('{} | {} | {} | {}'.format(item[0], item[1], item[2], item[1] * item[2]))
    soma += item[1] * item[2]
print('-' *20)
print(f'Total a ser pago: {soma}')