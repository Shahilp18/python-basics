
#! Inheritance
#* Reusing attr & methods from a Parent(Base) class.

class School:
    start_time = "10am"
    end_time = "6pm"

class Teacher(School):
    def __init__(self, subject):
        self.subject = subject

t1 = Teacher("Python");
print(t1.subject, t1.start_time, t1.end_time)

#! Types of Inheritance 
#* Single Level Inheritance
#* MultiLevel Level Inheritance
class School:
    start_time = "10am"
    end_time = "6pm"

class Teacher(School):
    def __init__(self, subject):
        self.subject = subject

class Admin(Teacher):
    def __init__(self, subject, role):
        super().__init__(subject)
        self.role = role

a1 = Admin("CPP", "Manager")
print(a1.subject, a1.role, a1.start_time, a1.end_time)


#* Multiple Level Inheritance
class Teacher:
    def __init__(self, salary):
        self.salary = salary


class Student:
    def __init__(self, gpa):
        self.gpa = gpa


class TA(Teacher, Student):
    def __init__(self, salary, gpa, name):
        Teacher.__init__(self, salary)
        Student.__init__(self, gpa)
        self.name = name


ta1 = TA(15000, 9.3, "Shahil")

print(ta1.name, ta1.gpa, ta1.salary)
