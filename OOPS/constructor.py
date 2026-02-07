class Student:
    def __init__(self):  #? Default Constructor
        print("Constructor was called...")

    def __init__(self, name, cgpa): #? Para Constructor
        print("Constructor was called...")
        self.name = name
        self.cgpa = cgpa
    
    def get_cgpa(self):
        return self.cgpa

s1 = Student("Rahul", 8.2)
s2 = Student("Shahil", 9.9)

print(s1.name, s1.cgpa)
print(s2.name, s2.cgpa)

print(f"{s1.name} has got", s1.get_cgpa())

#* Do not create multiple constructors in one class like CPP or Java. If do so last constuctor will be taken valid
#* One class -> One init Method


 