n=int(input("Enter the th number want to add until: "))
def add(num):
  sum=0
  for i in range(0,num+1):
    sum=sum+i
  print(sum)  
  return sum
  
add(n)