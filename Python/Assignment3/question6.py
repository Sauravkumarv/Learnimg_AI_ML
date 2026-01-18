words =["apple","banana","kiwi","cherry","mango"]

dict={}
def Dict(w):
  for i in w:
    dict[i]=len(i)
  return print(dict)
    

Dict(words)