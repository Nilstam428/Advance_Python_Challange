class Car:
  def __init__(self,brand,model,color):
    self.Model = model
    self.Brand = brand
    self.Color = color
  
  def info(self):
    print("Car Details:")
    print(f"Brand: {self.Brand}")
    print(f"Model: {self.Model}")
    print(f"Color: {self.Color}")

car1 = Car("Toyota","Corolla","Red")
car1.info()

car2 = Car("Honda","Civic","Blue")
car2.info()

car3 = Car("Bmw","i3","Black")
car3.info()

print(id(car1))
print(id(car2))
print(id(car3))
