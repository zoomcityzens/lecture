class Employee:
    '''The init function creates the first initialisation
    of ther class in memory'''
    num_of_emp = 0
    def __init__(self, firstname, lastname, salary, gender):     
         self.firstname = firstname
         self.lastname = lastname
         self.salary = salary
         self.gender = gender
         self.mail = firstname + '.' + lastname + '@veritas.edu.ng'
         Employee.num_of_emp += 1
         
'The above are called instance variables. They specify the values that unique objects can access'
'The following are objects'
Employee1 = Employee('Joshua', 'Jibrin', 2000, 'Binary')
Employee2 = Employee('Clement', 'Alinko', 2500, 'Queer')
Employee3 = Employee('Clement', 'Alinko', 2500, 'Queer')

print(Employee1.lastname)
print(Employee2.gender)
print(Employee2.firstname)
print(Employee1.salary)
print(Employee2.firstname)
print(Employee.num_of_emp)


