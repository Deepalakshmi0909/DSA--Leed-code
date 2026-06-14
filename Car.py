class Car:
    no_of_wheels=0
    mileage=20
    no_of_airbags=0

    def moveforward():
        print("Car is moving")
        
    def moveBackward():
        print("Car is moving backward")

car1=Car()

print(car1.no_of_wheels)
print(car1.mileage)
print(car1.no_of_airbags)

car2=Car()
car2.mileage=25
print("Mileage",car2.mileage)
