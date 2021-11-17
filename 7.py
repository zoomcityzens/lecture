class Student:
    def __init__(self, name, mat_no, grade):
       self.name = name
       self.mat_no = mat_no
       self.grade = grade
       
    def get_grade(self):
        return self.grade
    
    
class Course:
    def __init__(self, course_name, total_std):
        self.course_name = course_name
        self.total_std = total_std
        self.students = []
           
    def add_student(self, student):
        if len(self.students) < self.total_std:
            self.students.append(student)
            return True
        return False
    
    def get_avg_grade(self):
        value = 0
        for student in self.students:
            value += student.get_grade()
        return value/len(self.students)
       
       
student1 = Student("John", "CSC08763", 78)
student2 = Student("Mary", "CSC0876fu3", 90)
student3 = Student("Esther", "CSC0876fsfu3", 90)

print(student1.name)

course1 = Course("COmp Architecture", 4)
course1.add_student(student1)
course1.add_student(student2)

print(course1.get_avg_grade())
