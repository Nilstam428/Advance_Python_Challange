class Student:
  def __init__(self, name,age,gender,grade,address):
    self.name = name
    self.age= age
    self.gender = gender
    self.grade = grade
    self.address = address

  def info(self):
    print(f"Name: {self.name}")
    print(f"Age: {self.age}")
    print(f"Gender: {self.gender}")
    print(f"Grade: {self.grade}")
    print(f"Address: {self.address}")

print("Student details:")

s1 = Student("Nilesh",22,"Male","A","Pune")
obj1 = Student("Ramesh", 34, "male", "C", "mumbai")
s1.info()
print(obj1.info())
print(id(obj1))

# print("\n")
