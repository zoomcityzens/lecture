#To get the average grades and number 
# of registered students in a course

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
    
    def Calc_Avg_Grade(self):
        value = 0
        for student in self.students:
            value+= student.get_grade()
        return value/len(self.students)
    
student1 = Student("Jibrin", "CSC2344", 79)
student2 = Student("Christiana", "CSC4533", 78)
student3 = Student("Mofetoluwa", "CSC97864", 90)
student4 = Student("Rume", "CSC13234", 100)

course1 = Course("OOP in Python", 67)
course2 = Course("COmputer Architecture", 10)
course3 = Course("Data Science", 45)


course1.add_student(student1)
course1.add_student(student2)
course1.add_student(student3)
course1.add_student(student4)

course2.add_student(student1)
course2.add_student(student2)
course2.add_student(student3)

print(course2.Calc_Avg_Grade())
print(course1.Calc_Avg_Grade())

