class Person:
    def __init__(self): 
        self.firstname = input('Enter first name:  ')
        self.lastname = input('Enter last name:  ')
    def show_full_name(self): 
        return self.firstname + ' ' + self.lastname 
    #creating an object with the classperson2 = Person() person2.show_full_name()

person1 = Person()
print(person1.firstname)
print(person1.lastname)