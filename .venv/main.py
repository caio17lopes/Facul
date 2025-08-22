from Codigo.AnimalFactory import AnimalFactory

new_dog = AnimalFactory.new_animal(animal_type='dog', height=20, weight=10, age=1)
print(new_dog.age)