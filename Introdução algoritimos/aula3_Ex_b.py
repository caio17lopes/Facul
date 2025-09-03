'''
ma loja de departamentos está oferecendo diferentes formas de pagamento, conforme opções listadas a seguir. 
Faça um algoritmo que leia o valor total de uma compra e calcule o valor do pagamento final de acordo com a opção escolhida.

Se a escolha for por pagamento parcelado, calcule também o valor de cada parcela. 
Ao final, apresente o valor total da compra e o valor das parcelas:

Pagamento à vista – conceder desconto de 5%;
Pagamento em 3x – o valor não sofre alterações;
Pagamento em 5x – acréscimo de 2%;
Pagamento em 10x – acréscimo 8%.
'''
print('PAGAMENTO')
print('1 - à vista')
print('2 - parcelado 3x')
print('3 - parcelado 5x')
print('4 - parcelado 10x')

op= int(input('Selecione a forma de pagamento: '))
valor = float(input('Informe o valor da compra: '))

if (op == 1):
    valor_final = valor * 0.95
    print(f' Sua compra ficou o valor de {valor:.2f}, como o metodo foi pagamento a vista você tem o desconto de 5% ficando {valor_final:.2f}')
elif (op == 2):
    valor_final = valor 
    parcelamento = valor_final / 3
    print(f'Sua compra ficou no valor de {valor:.2f} o metodo de pagamento foi parcelamento, ficando em 3x de {parcelamento:.2f} ')
elif (op == 3):
    valor_final = valor * 1.02 
    parcelamento = valor_final / 5
    print(f'Sua compra ficou no valor de {valor:.2f} o metodo de pagamento foi parcelamento ficando em 5x de {parcelamento:.2f} por conta do acrescimo de 2% \
o valor total da sua compra ficou {valor_final:.2f}')
elif (op == 4):
    valor_final = valor * 1.08
    parcelamento = valor_final / 10
    print(f'Sua compra ficou no valor de {valor:.2f} o metodo de pagamento foi parcelamento ficando em 10x de {parcelamento:.2f} por conta do acrescimo de 8% \
o valor total da sua compra ficou {valor_final:.2f}')
else:
    print('OPERAÇÃO INVALIDA!')