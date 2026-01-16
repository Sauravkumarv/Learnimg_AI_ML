n=int(input("Enter the number want to calculate digits: "))

def countNum(num):
    count=0
    while(num>0):
     rem=int(num%10)
     count+=1
     num=int(num/10)

    return print(count)
countNum(n)