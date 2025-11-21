class Person:
  def __init__(self,name,age,gender,address,phone_no):
    self.name = name
    self.age = age
    self.__gender = gender
    self._address = address
    self.__phone_no = phone_no

  def get_info(self):
    print(f"Name: {self.name}")
    print(f"Age: {self.age}")
    print(f"Gender: {self.__gender}")
    print(f"Address: {self._address}")
    print(f"Phone No: {self.__phone_no}")

  def set_info(self,name,age,gender,address,phone_no):
    self.name = name
    self.age = age
    self.__gender = gender
    self._address = address
    self.__phone_no = phone_no

person1 = Person("Nilesh",21,"Male","Pune",1234567890)
# person1.get_info()
person1.set_info("Nilesh",22,"Male","Pune",1234567890)
person1.get_info()

print(person1._address)