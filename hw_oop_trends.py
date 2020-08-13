# Declare the class / type


class Student():
    # properties
    # HW1: add property "grades" -> list, grades = []
    name = None
    spec = None
    grades = []

    # methods

    def setProps(self, n, s, g):
        self.name = n
        self.spec = s
        self.grades = g

    # HW: add method "CalculateAvgGrade()" grades -> calculate average

    def CalculateAvgGrade(self):
        average_len = (len(self.grades))
        avg_grade = sum(self.grades) / average_len
        print(f"My Average Grade is:  {avg_grade:4.2f}")
        print(f'='*27)

    def sayHi(self):
        print(f'='*27)
        print("HELLO! I am a student!")
        print(f"My Name is {self.name}. \nMy Speciality is {self.spec}.")
        print(f'='*27)
        print("My grades: ")
        print(f'='*10)
        for i in range(len(self.grades)):
            if self.grades[i] >= 0 and self.grades[i] <= 10:
                print(f"{self.grades[i]:4.1f}")
                print("*"*5)
        print(f'='*27)


# 2. create an object of this type

s1 = Student()
s1.setProps("Ion", "MIT", [9.3, 7.4, 9.8, 6.4, 9.1, 9.1, 7.8, 8.6, 10.0, 7.1, 10.0, 9.98, 8.6])
s2 = Student()
s2.setProps("Maria", "FF", [10.0, 7.1, 9.1, 9.3, 7.4, 5.9, 9.8, 9.1, 7.8, 8.6, 5.9])
s3 = Student()
s3.setProps("Ivanov", "Biology", [9.1, 7.8, 8.6, 10.0, 9.1, 9.3, 7.4, 9.8, 8.1, 9.3, 7.4, 9.8, 9.1])
s1.sayHi()
s1.CalculateAvgGrade()
s2.sayHi()
s2.CalculateAvgGrade()
s3.sayHi()
s3.CalculateAvgGrade()
