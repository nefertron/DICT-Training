class Car:
    def __init__(self, make, model, year, engine) -> None:
        self.make = make
        self.model = model
        self.year = year
        self.engine = engine
        self.speed = 0
        print('Created new car')

    def accelerate(self):
        self.speed = self.engine * 100

    def brake(self):
        self.speed -= 10


car1 = Car('TOYOTA', 'Camry', 2023, 1.5)
car2 = Car('HONDA', 'Civic Type R', 1992, 1.3)


car2.accelerate()
car2.accelerate()

print(car1.speed)
print(car2.speed)
car2.brake()
print(car2.speed)