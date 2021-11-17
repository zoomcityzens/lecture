class Employee:
    num_of_emps = 0
    raise_amount = 1.04
    
    def __init__(self, first, last, salary):
         self.first = first
         self.last = last
         self.salary = salary
         self.mail = first + '.' + last + '@veritas.edu.ng'
         
         Employee.num_of_emps +=1
         
    def fullname(self):
        return self.first + self.last
    
    def salary_raise(self):
        self.pay = int(self.salary * self.raise_amount)
    
       
print(Employee.num_of_emps)  
emp_1 = Employee('Amina', 'Zaria', 60944)
emp_2 = Employee('Bola', 'Tinubu', 45899)
    


print(Employee.num_of_emps)
#print(Employee.__dict__)
# print(Employee.raise_amount)
# print(emp_1.raise_amount)
# print(emp_2.raise_amount)





