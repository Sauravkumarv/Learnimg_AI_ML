student={
    "Amit": 85,
    "Rohit": 78,
    "Saurav": 92,
    "Neha": 88,
    "Pooja": 74
}

def addStudent(stud):
  k=input("Enter the name of student: ")
  stud[k]=None
  print(stud)

  return ("Student added successfully",stud)

def updateMarks(stud):
  n=print("Enter the student name whose marks want to update!")
  nam=input("Enter the student name here: ")
  m=print("Enter the marks want to update!")
  mark=int(input("Enter you marks here: "))
  for name,marks in stud.items():
    if name==nam:
      stud[nam]=mark
    else:
      print("Student does't exists!")
      return
  return print(stud)

def searchStudent(stud):
  m=int(input("Enter marks here to search student: "))
  for name,marks in stud.items():
    if marks==m:
      print(name)
      return
  
  print("No student found with this mars!")
   
  return


  


def dispalyAll(stud):
  students=stud.items()
  return print(students)

def cntrl(stud,sc):
  if sc=='a':
    return addStudent(stud)
  elif sc=='d':
    return dispalyAll(stud)
  elif sc=='b':
    return updateMarks(stud)
  elif sc=='c':
    return searchStudent(stud)
  else:
    print("you have,nt select any input!")

print("**************Hey I am your student Manager!***************")    
print("Enter a to add a studen!")
print("Enter b to update marks!")
print("Enter c to Search for students!")
print("Enter d to Dispaly all students!")
sc=input("Enter here: ")

cntrl(student,sc)
  



