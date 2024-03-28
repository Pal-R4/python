class Person:
 def __init__(self, name, age):
    self.__private_attribute = 'This is a private attribute.'
    self.name = name
    self.age = age
 def display_protected_attributeprivate(self):
   print("name",self.name)
   print("pri",self.private_attribute)
person = Person('John Doe', 30)
print(person.__private_attribute)
print(person.__private)
