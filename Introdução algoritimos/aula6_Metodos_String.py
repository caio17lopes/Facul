# Trabalhando com métodos string 
'''
Manipular strings é um assunto bastante vasto
Nesta aula você aprendeu os conceitos de lista e de métoo, o que nos permite estudar mais a fundo as strings
UMA STRING É IMUTÁVEL
Mas, com listas, podemos alterá-la
'''
s1 = 'Algoritimos'
print(s1)
#s1[0] = 'a' comentei aqui pq da erro

s1 = list('Algoritimos')
print(s1) # print separdo
print(''.join(s1)) # print agrupado

s1 [0] = 'a'
print(''.join(s1))


# Verificando caracteres 
'''
.count() conta quantas letras ou palvras repentem
.lower() deixa todas as letras minusculas
.upper() deixa todas as letras maiusculas
.title() deixa so as primeiras letras maisuculas
.center() centraliza uma string
'''