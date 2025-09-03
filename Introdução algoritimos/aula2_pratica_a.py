'''
Aula pratica de atribuição 
    a) Atribuir o valor inteiro 3 à variável
    b) atribuir o valor 4 à variável
    c) Atribuir à variavel c o valor da expressão a*a + b*b
'''
a = 3
b = 4
c = a*a+b*b
print(c)

####### Strings #######
# Execute as seguintes atribuições 
#s1 = 'ant'
#s2 = 'bat'
#s3 = 'cod'
# Agora, utilizando operadores + e *, crie as saídas a seguir:
# a) 'ant bat cod'
s1 = 'ant'
s2 = 'bat'
s3 = 'cod'
res = s1 + ' ' + s2 + ' ' + s3
print (res)

# b) 'ant ant ant ant ant ant ant ant ant ant '

res = 10* (s1 + ' ')
print (res)

# c) 'ant bat bat cod cod cod'
res = s1 +' '+ 2* (s2 + ' ') + 3* (s3 + ' ')
print (res)

# d) ' ant bat ant bat ant bat ant bat ant bat ant bat ant bat'
res = 7 * ('ant'+' '+'bat'+ ' ')
print (res)

#  e) ' batbatcod batbatcod batbatcod batbatcod batbatcod'
res = 5*((2*s2)+s3 +' ')
print (res)