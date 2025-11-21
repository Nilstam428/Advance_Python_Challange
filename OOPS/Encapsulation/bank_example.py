class Bank:
  def __init__(self, name, balance, ID, pin):
    self.name = name 
    self._balance = balance
    self.ID = ID
    self.__pin = pin
    
    def deposit(self, amount):
      if amount>0:
        self._balance += amount
      else:
        print("Invalid amount")
        
    def withdraw(self, amount):
      if amount>0 and amount<=self.balance:
        self._balance -= amount
      else:
        print("Invalid amount")
    
    def set_pin(self, new_pin):
      self.__pin = new_pin
      
    def get_details(self):
      """ Prints the details of the bank account. """
      print(f"Name: {self.name}")
      print(f"Balance: {self._balance}")
      print(f"ID: {self.ID}")
      
    def get_balance(self):
      return self._balance
    
    def get_pin(self):
      return self.__pin 
    
    def __str__(self):
      return f"Name: {self.name}\nBalance: {self._balance}\nID: {self.ID}"


customer = Bank("Nilesh", 1000, 14000, 1234)

# print(customer.get_details())
customer.get_details()