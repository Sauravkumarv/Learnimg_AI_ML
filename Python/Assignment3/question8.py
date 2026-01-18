list1 =[1,2,3,4] 
list2 =[5,3,7,8]

def check(func,list1,list2):
  s1=func(list1)
  s2=func(list2)

  if s1.intersection(s2):
    return print(True)
  else:
    return print(False)
    


def conversion(list):
  s=set()
  for i in list:
    s.add(i)

  return s


check(conversion,list1,list2)