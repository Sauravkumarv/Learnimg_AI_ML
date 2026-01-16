prime=int(input("Enter a number to check (is prime or not): "))

def checkPrime(prime):
  if(prime<2):
    return print("It is not a prime number!")
  count=0
  for i in range(1,prime+1):
    if(prime%i==0):
      count=count+1
  if(count==2):
    return print(True,"Yes its a prime number")
  else:
    return print(False,"No its not a prime number")
  
checkPrime(prime)
    

  