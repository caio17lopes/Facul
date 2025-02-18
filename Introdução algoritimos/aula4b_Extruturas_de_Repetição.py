# TÓPICOS IMPORTANTES COM LAÇOS EM PYTHON

soma = 0
cont = 1
while (cont <= 5):
    x = int(input(f'Digite o {cont}ª numero: '))
    soma += x # Equivalente : soma = soma + x
    cont += 1 # Equivalente : cont = cont + 1
print(f'Somatoria {soma}')

# VALIDANDO ENTRADAS COM UM LOOP

x = int(input('Digite um valor maior que zero: '))
while (x <= 0):
    x = int(input('Digite um valor maior que zero: '))
print(f'Você digitou {x}, encerrando o programa...')

# INSTRUÇÃO BREAK 