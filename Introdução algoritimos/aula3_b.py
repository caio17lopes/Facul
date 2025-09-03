# Expressões logicas e álgebras booleana
'''
Python       / Pseudocódigo   / Operação

not          / não            / negação
and          / e              / conjução
or           / ou             / disjunção

Operador not

Serve par anegar um resultado logico ou o resultado de uma expressão booleana
Na praica, isso significa que o resultado final de uma expressão sera invertido

V       /   not V
true    /   false
false   /   true

'''
x = True
y = False
print(x)
print(y)

'''
Operador and
v1      /   v2     /    v1 and v2

false   /   false   /   false
false   /   true    /   false
true    /   false   /   false      
true    /   true    /   true
'''

x = False
y = True
print(x and y)

'''
Operador or

v1      /   v2     /    v1 and v2

false   /   false   /   false
false   /   true    /   true
true    /   false   /   true      
true    /   true    /   true
'''

x = True
y = False
print (x or y )

'''
Procedência dos operadores ( sequência da operação)
1. Parênteses
2. Operadores aritméticos de potenciação ou raiz
3. Operadors aritméticos de multiplicação, divisão e modulo
4. Operadores aritméticos de adição e subtração
5. Operadores relacionais
6. Operadores lógicos not
7. Operadores lógicos and
8. Operadores lógicos or
9. Atribuições
'''
# Exercícios 

x = 10
y = 1
res = not x > y
print (res)

x = 10 
y = 1
z = 5.5
res (x > y) and (z == y) # True and False
print (res)

x = 10 
y = 1
z = 5.5
res = x > y or not z == y and y != y + z / x 
#res = True or not False and True
#res = True or True and True 
print(res)

# Pedir as notas dos alunos e fazer a media para saber se passaram ou não de ano 

m1 = float(input('Digite a nota do 1° materia'))
m2 = float(input('Digite a nota do 2° materia'))
m3 = float(input('Digite a nota do 3° materia'))

if m1 >= 7 and m2 >= 7 and m3 >= 7:
    print('O aluno está aprovado de ano')
else:
    print('O aluno não passou de ano')