def velhice(nome,idade):
    nomes = str(nome).title()
    anos = int(idade)
    if anos <= 35:
        print(f'Seu nome é: {nomes} ')
        print(f'Você é jovem {anos}')
    elif anos >= 36 and anos <= 59:
        print(f'Seu nome é: {nomes} ')
        print(f'Você é um coroa {anos}')
    else:
        print(f'Seu nome é: {nomes} ')
        print(f'Você é idoso {anos}')
    return nomes,anos


seu_nome = input('digite seu nome: ')
idade = int(input('Digite sua idade: '))
velhice (seu_nome,idade)