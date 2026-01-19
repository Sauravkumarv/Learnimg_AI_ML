class Herbivore:
  def __init__(self):
    print ("Eat Grass")

class Carnivore(Herbivore):
  def  __init__(self):
    super().__init__()
    print("Eat Meat")

class Omnivore(Carnivore):
  def __init__(self):
    super().__init__()
    print("Eat both grass and meat")

class Bear(Omnivore):
  def __init__(self):
    super().__init__()
    
   


bear=Bear()

