def realce ():
    print('|', '##' *11,'|')
    

def menu (pergunta,min,max):
    try:
        x = int(input(pergunta))
        if min <= x <= max: 
            return x
        else:
            print(f'Seleção incorreta, escolha entre {min} ou {max}')
    except ValueError:
        print('Erro: Digite um valor valido')
    except TypeError:
        print('Ocorreu um erro')

def celsius(temp):
    try:
        return temp * 1.8 + 32
    except ValueError:
        print('Digite apenas numeros!')

def fahrenheit (temp):
    try:
        return (temp - 32) / 1.8
    except ValueError:
        print('Digite apenas numeros!')



#Programa principal 

while True:
    realce()
    print('Conversor de temperatura')
    realce()
    print('1 - Converter Celsius para Farenheit')
    realce()
    print('2 - Converter Farenheit para Celsius')
    realce()
    print('3 - Sair')
    op =  menu ('Escolha a opção desejada: ',1,3)
    if op == 1:
        while True:
            print('Você escolheu conversão de Celsius para Farenheit')
            try:
                temp = float(input('Digite a temperatura em celsius: '))
                print (f'{temp}°c = {celsius(temp):.2f} ')
                break
            except ValueError:
                print('Digite um valor valido')
    
    elif op == 2:
        
        print('Conversão de Fahrenheit para Celsius')
        while True:
            try:
                temp = float(input('Digite a temperatura em farhenheit:'))
                print(f'{temp:.2f}°f = {fahrenheit(temp):.2f}')
                break
            except ValueError:
                print('Digite um valor valido')
    
    elif op == 3:
        print('Encerrando o programa')
        break