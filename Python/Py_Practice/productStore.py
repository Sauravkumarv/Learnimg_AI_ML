class product:
  count=0
  def __init__(self,name,price):
    self.name=name
    self.price=price
    product.count+=1
 
  def get_info(self):
    print(f"Price of {self.name} is Rs.{self.price}")
  
  @classmethod
  def get_count(cls):
    print(f"Total products are= {cls.count}")

  @staticmethod
  def Discounted_price(price,percent,name):
    d=price-(price*(percent/100))
    print(f"Discounted price of {name} is {d}")
  

p1=product("Phone",10_000)
p2=product("Laptop",80_000)
p3=product("Camera",120_000)

p1.get_info()
p1.Discounted_price(p1.price,12,p1.name)
product.get_count()