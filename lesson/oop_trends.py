# Declare the class / type

class Student():
    # properties
    # HW1: add property "grades" -> list, grades = []
    #    : add method "calculateAvgGrade()" grades -> calculate average
    name = None
    spec = None
    grade = None
    #methods
    def setProps(self, n, s, g):
        self.name = n
        self.spec = s
        if g >= 0 and g <= 10:
            self.grade = g
        else:
            print("Error, wrong grade!")
            
    def sayHi(self):
        print("HELLO! I am a student!")
        print(self.name, self.spec, self.grade)



# 2. create an object of this type

s1 = Student()
s1.setProps("Ion", "MIT", 10.0)
s2 = Student()
s2.setProps("Maria", "FF", 9.9)
s1.sayHi()
s2.sayHi()