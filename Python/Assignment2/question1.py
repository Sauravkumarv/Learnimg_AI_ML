salary=float(input("Enter you salary: "))
 
def calaculateSalary(sal):
   if(sal<30000):
       print(five(sal))
   elif(sal>30000 and sal<70000):
       print(fifteen(sal))
   else:
       print(twentyFive(sal))


def five(t):
   cal=t*5/100
   return cal  
def fifteen(t):
   cal=t*15/100
   return cal  
def twentyFive(t):
  cal=t*25/100
  return cal        

calaculateSalary(salary)  