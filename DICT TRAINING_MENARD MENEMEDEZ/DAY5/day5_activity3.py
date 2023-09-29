class Person:
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age

    def greet(self):
        print(f'Hello my name is {self.name} and I am {self.age} years old')


person1 = Person('Gem Rey', 23)
person2 = Person('Menard', 25)

print(person1.name)
print(person2.name)

person1.greet()
person2.greet()