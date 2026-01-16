info=[
  ("Alice","Math"),
  ("Bob","Science"),
  ("Alice","Science"),
  ("Charlie","Math"),
  ("Bob","Math"),
  ("Alice","English"),
  ("Charlie","English"),
  ]

# set=set()

#Part 1
# *****************
# for tup in info:
#   # print(tup[1])
#   set.add(tup[1])
  
# print(set)

# ********or*******
# for name,coures in info:
#     set.add(coures)

# print(set)  


# question 2
# **********************
for name,course in info:
    if(course=="Science"):
        print(name)


#  question 3
# ************************
dict={}
for name,course in info:
    if(dict.get(name)==None):
        dict.update({name:set()})
        dict[name].add(course)
    else:
        dict[name].add(course)
print(dict)        