#Resolução de problemas

# Desenvolva um algortitimo que solicite ao usuário o preço de um produto e um percentual de desconto a ser aplicado a ele. Calcule e exiba o valor do 
# desconto e o preço fina ldo produto 


#preco = float (input('Digite o preço do produto: '))
#percentual = float (input('Digite o percentual de desconto: (0-100%): '))

#desconto= preco *(percentual /100 ) 
#final = preco - desconto 
#print(f'O preço do produto é {preco}. Desconto de {percentual}%')
#print(f'Valor calculado de desconto: {desconto}. Valor final do produto: {final}')

'''
Exercício 2 

Escreva um programa que pergunte a quantidade de km percorridos pro um carro alugado pelo usuário, assim como a quantidade de dias pelos quais o carro foi alugado.
Calcule o preço a pagar, sabendo que o carro custa R$ 60,00 por dia e R$ 0,15 porkm percorrido
'''

km = float(input('Quantos km foram percorridos? '))
diaria = int(input('Quantidade de dias que o carro foi alugado: '))
preco_km = float (0.15)
valor_km = float (km * preco_km)
preco_diaria = diaria * 60
# jeito mais rapido 
'''
km = int (input('Quantos km foram precorridos?'))
dias = int(input('Quantos dias foram percorridos'))
preco = 60* dias + 0.15 * km
print(f'KM = {km}. Dias: {dias}')
print (f'Valor a ser pago {preco}')

'''
print(f'A quantidade de km percorridos pelo cliente foi {km} km, o valor por km percorrido é de R$0.15, o valor fico {valor_km}')
print(f'O valor da diaria é de R$60,00 o cliente ficou {diaria} dia(s) com o carro dando um total de {preco_diaria}')
print('O valor total a ser pago pelo cliente é de R$',preco_diaria + valor_km)
