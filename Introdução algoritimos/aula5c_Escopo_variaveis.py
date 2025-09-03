#Escopo variaveis
'''
Escopo de uma variavel é a propiedade que determina onde uma variavel pode ser utilizada dentro de um programa
'''
# Escopo local
'''
Criado sempre que uma função é chamada
Variáveis criadas, seja no campo de um parâmetro ou dentro do corpo da função
e são chamada de variáveis locais. Essas variáveis só existem dentro daquela própia função
'''
#Escopo Global
'''
Craido no programa principal
Variáveis globais pertecem a um escopo global e são variaveis criadas dentro do programa principal.
Uma variável global existe também em todas funções invicadas ao longo do programa
'''
ovos = 0 # ignorar essa variável, esta aqui apenas para tirar o erro
def omelete ():
    ovos = 12 # variável local
#Program principal
omelete()
print(ovos)# Escopo global
# Dara um erro porque ovos so existe dentro do escopo local

def omelete ():
    print(ovos) # escopo local # Ovos é global mas uma função consegue acessar todas as variáveis globais

ovos = 12 # variável global
omelete()

def omelete ():
    ovos = 12
    bacon ()
    print(ovos)

def bacon():
    ovos = 6
omelete() # O resultado vai dar 12 porque mesmo tendo 2 def ovos, cada uma existe apenas dentro do escopo local, sendo assim não influencia uma na outra

def omelete():
    ovos = 12 # variável local de omelete
    print('Ovos = ', ovos)
def bacons ():
    ovos = 6 # variável local de bacon
    print('Ovos = ', ovos)
    omelete()
    print('Ovos= ', ovos)
ovos = 2
bacon()
print('Ovos = ', ovos)
# Instrução global
'''
Força o nosso programa a não criar uma variável local de mesmo nome e manipular somente a global dentro de uma função
'''
def omelete():
    global ovos 
    ovos = 6
ovos = 12
omelete()
print(ovos)

##################################################
def omelete():
    global ovos 
    ovos = 6
    bacon()
def bacon():
    ovos = 12 # Essa variavel do bacon não tme poder de altera o valor de ovos porque nao tem a instrução Global para alterar o valor de ovos vai ser sempre 6
    pimenta()
def pimenta():
    print(ovos)
# Programa principal
ovos = 4
omelete()
print(ovos)

########################################
def omelete():
    print(ovos)# Vai dar erro pq o print esta antes da variável o programa ainda não conhece a variável local ovos  
    ovos = 6
    
ovos = 12
omelete()