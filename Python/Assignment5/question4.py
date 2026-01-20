import json
dict={}
i=3
while i>0:
  city=input("Enter city name: ")
  popu=int(input("Enter popuulation"))
  dict[city]=popu
  i-=1

with open("cities.json","w") as f:
  json.dump(dict,f,indent=4,sort_keys=True)

#***************get_data****************
# with open("cities.json","r") as f:
#   data=json.load(f)  
#   print(data)