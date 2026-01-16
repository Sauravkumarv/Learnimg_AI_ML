palin=input("Enter a word to check palindrom or not: ")

def chec(palin):
  start=0
  end=len(palin)-1
  while(start<=end):
    if(palin[start]!=palin[end]):
      return print("It is not a palindrom")
      
    else:
      start+=1
      end-=1
  return print("It is palindrom")

chec(palin)
