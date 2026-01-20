w1="python"
indicator=True
count=1

with open("D:\AI_ML\Python\Py_Practice\search.txt","r") as f:

 while indicator:
   word=f.readline()
   if(w1 in word):
    print(f"Word found at line no {count}")
    break
   count+=1

  