cadastro = {'nome':[],'sexo':[],'idade':[]}
qtd = 0
while True:
    terminar = input('Deseja cadastrar mais alguma pessoa? [S/N] ')
    if terminar.upper() in 'N':
        break
    if terminar.upper() not in 'S':
        print('Digite S para SIM ou N para NÃO')
        continue
    nome = input('Qual o nome? ')
    sexo = input('Qual o sexo? ')
    idade = int(input('Qual o ano de nascimento: '))
    cadastro['nome'].append(nome.title())
    cadastro['sexo'].append(sexo.upper())
    cadastro['idade'].append(idade)
    qtd += 1 
print(cadastro)
print(f'Qtd de cadastro {qtd}')
media = sum(cadastro['idade']) / len(qtd)
print(f'Idade media dos cadastros: {media} anos')

