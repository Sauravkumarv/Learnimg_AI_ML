class Player:
  player_count=0
  def __init__(self,name,level):
    self.name=name
    self.level=level
    Player.player_count+=1
   
  @classmethod
  def get_count(cls):
    count= cls.player_count
    return count
  
p=Player("Saurav",5)
p=Player("Saurav",5)
p=Player("Saurav",5)
p=Player("Saurav",5)
p=Player("Saurav",5)

print(p.get_count())