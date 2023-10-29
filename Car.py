class Car:
    def __init__(self, make, model, year, speed):
        self.make = make
        self.model = model
        self. year = year
        self. speed = speed

    def accelerate(self, speedToAdd):
        self.speed+= speedToAdd
        print("The " + self.make + " " + self.model + "current speed: " + str(self.speed) + "km/h")


    def brake(self, speedToReduce):
        self.speed-=speedToReduce
        print("The " + self.make + " " + self.model + "current speed: " + str(self.speed) + "km/h")

car1 = Car("Jeep", "Sportcar", 2020, 40)
car1.accelerate(20)
car1.brake(30)

