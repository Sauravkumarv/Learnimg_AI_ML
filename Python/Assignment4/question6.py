from abc import ABC,abstractmethod
class Employees(ABC):
    @abstractmethod
    def calculate_salary(self):
        pass
    
class Intern(Employees):
    def calculate_salary(self):
        return 10_000
class FullTimeEmployee(Employees):
    def calculate_salary(self):
        return 30_000
class ContractEmployee(Employees):
    def calculate_salary(self):
        return 50_000
    
intern=Intern()
fullTime=FullTimeEmployee()
contract=ContractEmployee()

print(f"Inter Salary is: {intern.calculate_salary()}")  
print(f"Full Time Employee Salary is: {fullTime.calculate_salary()}") 
print(f"Contract Salary is: {contract.calculate_salary()}")       

