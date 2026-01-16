def createTup(n):
  t=()
  for i in range(n):
    value=int(input("Enter the number: "))
    t=t+(value,)
  return t

def even(tup):
  t1=()
  j=0
  for i in tup:
    if i%2==0:
      t1=t1+(i,)
      j+=1

  return t1
def odd(tup):
  t=()
  for i in tup:
    if i%2 != 0:
      t=t+(i,)
  return t


def main():
  n=int(input("Enter the nuber to create that much of tuple: "))
  i=createTup(n)
  e=even(i)
  o=odd(i)
  print("Even in tuples are: ",e)
  print("Odd in tuples are: ",o)
  return 

  
        

main()