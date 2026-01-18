list=[487,1,51,5,1,5,4]

def moreThanOnce(l1):
  l1.sort()
  count=0
  for i in range(len(l1)-1):
   if l1[i]==l1[i+1]:
    count+=1
  if count!=0:
    return print(count)
  return print("There is no any repeated number here!")

moreThanOnce(list)