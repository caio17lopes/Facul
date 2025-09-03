'''
Herença 
    Porqeu utilizar herença 
    No que difere das demais linguagens?
    Exemplos de uso 
    Eleborar programa com a classe Dog que recebe/herda da classe animal 
    Palavra- chave Super vs nome da calsse Pai 
    Sobrescrevendo metodos 
'''
class Animal:
    def __init__(self, age: int, heigth: int, weight: int, position: tuple):
        self.age = age
        self.heigth = heigth
        self.weight = weight
        self.position = position
    
    def move_x(self):
        self.position[0] +=1

    def move_y(self):
        self.position[1] +=1

    def move_z(self):
        self.position[2] +=1

class Dog(Animal):
    def __init__(self, age: int, heigth:int, weight:int, position: tuple):
        Animal.__init__(self,age, heigth, weight, position)

    def move_z(self):
        self.position[2] += 2

caramelo = Dog (10,40,30(0,0,0)) # pode ser escrito assim tambem ( age = 10, height = 50, wight = 30, position (0,0,0))
print(caramelo.age)