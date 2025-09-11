class Student:
    def __init__(self,name,roll_no,marks):

        self.name=name
        self.roll_no=roll_no
        self.marks=marks
    def display(self):
        print(f"student {self.name} of {self.roll_no} is {self.marks}")
students=[]
n=int(input())
for i in range(n):
    name=input("enter name:")
    roll_no=int(input("enter roll:"))
    marks=float(input("enter marks:"))
    s=Student(name,roll_no,marks)
    students.append(s)
for i in students:
    i.display()