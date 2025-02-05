# Comando input ('mensagem')

idade = input('Qual a sua idade? ')
print(idade)
nome = input ('Qual o seu nome? ')
print(f'Olá {nome}, seja bem vindo!')

# Convertendo dados de entrada (casting)
# O input sempre retorna em string, então é importante fazer o tratamento dos dados, fazendo uma conversão

nota = float (input('Qual noa você recebeu na disciplina? '))
print (f'Você tiro a nota {nota}')

# Fluxo de execução do program e o teste de mesa 
x = 1
y = 1
z = x+y

x = x + 2
y = y - 1
z = x + y 

x = y + 1
y = x - 1 
z = x + y
print (z)