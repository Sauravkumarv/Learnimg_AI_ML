class BankAccount:
  def __init__(self,acc,name,balance):
    self.acc=acc
    self.name=name
    self.balance=balance

  def set_deposite(self,amount):
    deposite=self.balance+amount
    return deposite

  def set_withraw(self,amount):
    withdrawl=self.balance-amount
    return withdrawl
  
  def get_balance(self):
    check=self.balance
    return check




acc=BankAccount(102020,"Saurav",10_0000)

print(f"New account Added: Account Number:{acc.acc}, Name: {acc.name}, Deposited: {acc.balance}")
print("Total Balance: ",acc.get_balance())
print("Remaining Amount is: ",acc.set_withraw(500))
print(f"Deposited Successfully,Total Balance is :{acc.set_deposite(1500)}")

    