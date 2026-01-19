class Person:
  # def __init__(self,name):
  #   self.name=name
  # def __init__(self,name,age):
  #   self.name=name
  #   self.age=age
    
  def __init__(self,name,age=None,address=None):
    self.name=name
    self.age=age
    self.address=address


person=Person("Saurav")
person=Person("Saurav",22)
person=Person("Saurav",22,"Ayanagar")

print(f"Biodata Name: {person.name}")
print(f"Biodata Name: {person.name}, Age: {person.age}")
print(f"Biodata Name: {person.name}, Age: {person.age}, Address: {person.address}")