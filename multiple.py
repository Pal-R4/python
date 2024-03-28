class Animal:
 def __init__(self, name):
  self.name = name
 def speak(self):
   return "Unknown sound"
class Lion(Animal): # Lion class inherits from Animal class
 def speak(self):
  return "Roar!"
class Tiger(Animal): # Tiger class inherits from Animal class
 def speak(self):
  return "Growl!"
# Create instances of subclasses
lion_instance = Lion("King")
tiger_instance = Tiger("Tony")
# Call the speak method of the subclasses
print(lion_instance.speak()) # Output: Roar!
print(tiger_instance.speak())
print(lion_instance.name)