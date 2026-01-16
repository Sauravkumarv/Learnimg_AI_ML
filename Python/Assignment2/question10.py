n=int(input("Enter your number and we'll check how far or near it is of secret number: "))
secret=19

def guessGame(n,secret):
  if(n>secret):
   return print("Too High")
  elif(n<secret):
    return print("Too Low")
  else:
    print("Correct!")
guessGame(n,secret)