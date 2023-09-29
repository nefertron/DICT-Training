class Animal:
    def __init__(self, name, species) -> None:
        self.name = name
        self.species = species

    def speak(self):
        print(f'{self.name} is an {self.species} and makes a sound.')


class Dog(Animal):
    def __init__(self, name, breed) -> None:
        super().__init__(name, species='Dog')
        self.breed = breed

    def speak(self):
        print(f'{self.name} is a {self.breed} dog and barks')




class Cat(Animal):
    def __init__(self, name, color) -> None:
        super().__init__(name, species='Car')
        self.color = color

    def speak(self):
        print(f'{self.name} is a {self.color} cat and meows')



dog = Dog('Pudding', 'Golden Retriever')
cat = Cat('Angel', 'Gray')

dog.speak()
cat.speak()