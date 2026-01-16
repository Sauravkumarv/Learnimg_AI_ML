def mList(n):
  list=[]
  for i in range(n):
    list.append(input("Enter your Integer: "))
  return list



def merge(func,n1,n2):
  fn1=func(n1)
 
  fn2=func(n2)
  j=fn1+fn2
  return print(j)

n1=int(input("Enter the number of Integer do you want in list1: "))
n2=int(input("Enter the number of Integer do you want in list2: "))


merge(mList,n1,n2)
  
  
