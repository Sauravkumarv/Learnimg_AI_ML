list=[5,10,15]

def computeAvg(list):
  sum=0
  for i in list:
    sum=sum+i
  return print(sum/len(list))

computeAvg(list)