# Condicional Simple
'''
Traduza as afirmações a seguir para condicionais em python

a) Se idade é maior que 60, escreva: " VocÊ tem direitos aos benefícios".
b) Se dano é maior que 10 e escudo é igual a 0, escreva:"Você esta morto!"
c) Se pelo menos uma das variáveis booleanas norte, sul, leste e oeste resultarem em True, escreva: "Você escapou!"
'''
idade = int(input('Informe a sua idade: '))
if idade >= 60:
    print(f'Você tem {idade} por isso tem direitos aos benefícios')
else:
    print(f'Você tem a idade de {idade}, por isso não terá direito aos benefícios')

dano = int(10)
escudo = int(input('Informe de 1 à 10 qual a resistência do seu escudo: '))
if dano > escudo : 
    print(f'You die. Seu escudo so resiste a {escudo}, o dano que levou foi de {dano}')
else:
    print(f'You alive. O dano foi de {dano}, e a resistencia do seu escudo é de {escudo}')

norte = True
sul = False
leste = False
oeste = False

if (norte == True or sul == True or leste == True or oeste == True):
    print('Você escapou')

'''
PRATICA
Se ano divisivel por 4 = ano bissesto
Se não, não é ano bissesto
'''
ano = int(2026)

if (ano % 4 == 0):
    print('É um ano bissesto')
else:
    print('Não é um ano bissesto')

cima = True
baixo = True
if (cima == True and baixo == True):
    print('Decida-se')
else:
    print('Você escolheu um camino compadre')