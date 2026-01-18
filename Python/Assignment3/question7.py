user=input("Enter you words and I'll find the sapce in your string: ")

def sapce(sp1):
  sp=sp1.split(" ")
  if len(sp)==0:
    return print("There is no space in words!")
  else:
    count=len(sp)-1
  return print(f"ther is {count} space in between")

sapce(user)
