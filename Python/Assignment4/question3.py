class Student:
  def __init__(self,name,roll_no,marks):
    self.__name=name
    self.__roll_no=roll_no
    self.__marks=marks
  
  def get_name(self):
    return self.__name
  
  def get_roll_no(self):
    return self.__roll_no
 
  def get_marks(self):
    return self.__marks
  
  def set_name(self,name):
    if name==" ":
      return print("Name Cannot be Empty!")    
    name=self.__name=name
    return name
  
  def set_roll_no(self,roll_no):
    if roll_no<1 or roll_no>100:
      return print("Roll No should be between 1 to 100")
    roll_no=self.__roll_no=roll_no
    return roll_no
 
  def set_marks(self,marks):
    if marks<0:
      return print("Marks cannot be negative!")
    marks=self.__marks=marks
    return marks
  

stud=Student("Saurav",1,95)
print(stud.get_name(),stud.get_roll_no(),stud.get_marks())
print(stud.set_marks(120))
print(stud.set_name("Rahul"))
print(stud.set_roll_no(5))