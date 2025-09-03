'''
Classes

    Atributos especiais 
        _name_
        _class_

    Especificar o tipo de atributo 
        (self._atrubuto : int)

    Criação de metodos 
    Passagens de parametros sem tipo definido 
    Passagem de parametros com tipo definido 
    MEtodos preotegido:_metodo(self)
    Metodos especial : _init_ 

'''
# class Dog:
#     def __init__(self):
#         pass

# #main 
# rex = Dog()
# print(rex)

# 2B - Inserir Atributos  com valor fixo 

# class Dog:
#     def __init__(self): # o __ refere-se a metodos especiais inv. automanticamente em situações especiais 
#         self.age = 5

# #main 
# rex = Dog()
# print(f'A idade do rex é : {rex.age}')
# caramelo = Dog()
# print(f'A idade do carmelo é: {caramelo.age}')

#2C Inserir atributos com passagem de paramentros no construtor da class 

# class Dog:
#     def __init__(self,age): # o __ refere-se a metodos especiais inv. automanticamente em situações especiais 
#         self.age = age

# #main 
# rex = Dog(10)
# print(f'A idade do rex é : {rex.age}')
# caramelo = Dog(5)
# print(f'A idade do carmelo é: {caramelo.age}')

#2D - Atributo da classe

# class Dog:
#     family ='Canidae'
#     def __init__(self,age): # o __ refere-se a metodos especiais inv. automanticamente em situações especiais 
#         self.age = age

# #main 
# rex = Dog(10)
# print(f'A idade do rex é : {rex.age} e pertence a familia {rex.family}')
# caramelo = Dog(5)
# print(f'A idade do carmelo é: {caramelo.age} e pertence a familia {caramelo.family}')
# print(f'A familia que pertence a todos os cachorros é {Dog.family}')

# 2E Definindo o tipo de um atributo 

# class Dog:
#     family ='Canidae'
#     def __init__(self,age: int): # o __ refere-se a metodos especiais inv. automanticamente em situações especiais 
#         self.age:int = age
#         self.age.real

# #main 
# rex = Dog(10)
# print(f'A idade do rex é : {rex.age} e pertence a familia {rex.family}')
# caramelo = Dog(5)
# print(f'A idade do carmelo é: {caramelo.age} e pertence a familia {caramelo.family}')
# print(f'A familia que pertence a todos os cachorros é {Dog.family}')

# print(f'Rex é um objeto de qual classe? R: {rex.__class__.__name__}')
# print(f'Caramelo é um objeto de qual classe? R: {caramelo.__class__.__name__}')

#2G- Atributos protegidos
# class Dog:
#     family = 'Canidae'
#
#     def __init__(self, age, peso):  # o __ refere-se a métodos especiais inv. automaticamente em situações específicas.
#         self.__age = age  # _ uma dica que é um atributo privado e que não deve ser modificado diretamente fora da classe
#         self._peso = peso  # __ o interpretador Python realiza uma "mangling", evitar colisão de nomes.
#
#
# # ----main
# rex = Dog(10, 45)
# print(f'Rex - idade: {rex._age}, peso: {rex._peso} a pertence a família: {rex.family}')
# caramelo = Dog(5, 30)
# print(f'Caramelo - idade: {caramelo._age}e a pertence a família: {rex.family}')
#
# print(f'A que familia pertence todos os cachorros: {Dog.family}')

# 2H - Utilizando métodos
#
# 2G- Atributos protegidos
# class Dog:
#     family = 'Canidae'
#
#     def __init__(self, age):  # o __ refere-se a métodos especiais inv. automaticamente em situações específicas.
#         self._age = age  # _ uma dica que é um atributo privado e que não deve ser modificado diretamente fora da classe
#         self.__peso = 0
#
#     def get_age(self) -> int:  # pode se definir o dado de retorno
#         return self._age

    # def get_peso(self) -> int:  # pode se definir o dado de retorno
    #     return self.__peso
#
#     def set_peso(self, peso: int): # pode se definir o dado de entrada
#         self.__peso = peso
#
#
# # ----main
# rex = Dog(10)
# rex.set_peso(45)
# print(f'Rex - idade: {rex.get_age()}, peso: {rex.get_peso()} a pertence a família: {rex.family}')
# caramelo = Dog(5)
# caramelo.set_peso(30)
# print(f'Caramelo - idade: {caramelo.get_age()}e a pertence a família: {rex.family}')
#
# print(f'A que familia pertence todos os cachorros: {Dog.family}')