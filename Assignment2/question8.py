print("Hey I am your Calculator")
print("Write 1 to Add")
print("Write 2 to Sub")
print("Write 3 to Mul")
print("Write 4 to Div")
operation=int(input())

def caculate(operation):
  match operation:
    case 1:
      add()
      return
    case 2:
      sub()
      return
    case 3:
      mul()
      return
    case 4:
      div()
      return
    case _:
      print("Sorry you hav'nt choose any option!")


def add():
  a=int(input("Enter a: "))
  b=int(input("Enter b: "))
  sum=a+b
  return print("Sum of a and b: ",sum)

def sub():
  a=int(input("Enter a: "))
  b=int(input("Enter b: "))
  sub=a-b
  return print("Sub of a and b: ",sub)
def mul():
  a=int(input("Enter a: "))
  b=int(input("Enter b: "))
  mul=a*b
  return print("Mul of a and b: ",mul)
def div():
  a=int(input("Enter a: "))
  b=int(input("Enter b: "))
  div=a/b
  return print("Div of a and b: ",div)
caculate(operation)
