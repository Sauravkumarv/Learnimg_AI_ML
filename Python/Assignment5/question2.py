# with open("log.txt","w") as f:
#   num=int(input("number of logs: "))
#   while num>0:
#     log=input("Logs")
#     f.write(f"{log}\n")
#     num-=1

# **********APPEND FILE ********

# with open("log.txt","a") as f:
#   f.write("Program run Successfully")

# *********PRINT ALL FILE **********
# with open("log.txt","r") as f:
#   data=f.read()
#   print(data.strip())

# ***********or**********
with open("log.txt","a+") as f:
  f.write("End of program2\n")
  f.seek(0)
  print(f.read())