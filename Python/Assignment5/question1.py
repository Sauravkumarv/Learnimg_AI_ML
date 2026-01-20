# with open("names.txt","w+") as f:
#   number=int(input("how many names do you want to write: "))
#   while(number>0):
#     n=input("Write name here: ")
#     f.writelines(f"{n}\n")
#     number-=1
with open("names.txt","r") as f:
    data=f.read()
    print(data.strip())
  

 
 
  

    
  


 