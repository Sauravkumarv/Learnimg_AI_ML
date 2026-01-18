class Book:
  def  __init__(self,title,author,reviews):
    self.__title=title
    self.__author=author
    self.reviews=reviews

  # def set_title(self):

  def set_reviews(self,reviews):
     self.reviews.append(reviews)
     return reviews
     
  def count_review(self):
    count=len(self.reviews)
    return count
  def get_reviews(self):
    return self.reviews

  def get_title(self):
    return self.__title

  def get_author(self):
    return self.__author
  

book=Book("Blind Man","SK_Verma",["Loved It"])

print(f"New Review Added is: {book.set_reviews("Amazing")}")
print(f"New Review Added is: {book.set_reviews("Nice")}")
print(f"Book details Title: {book.get_title()}, Author: {book.get_author()} , Reviews: {book.get_reviews()}")
print(f"Total Reviews are: {book.count_review()}")