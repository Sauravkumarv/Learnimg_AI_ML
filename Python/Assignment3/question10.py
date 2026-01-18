write=input("Enter a String to find a unique characters: ")


def unique(write):
  unique=[]
  for i in write:
    if i not in unique:
      unique.append(i)
  print(unique)
  return print(len(unique))


unique(write)