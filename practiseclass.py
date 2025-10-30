# Create a class name student that stores name, roll number and marks of 3 subjects. Create Methods to calculate the total & average marks of the student. Display Result of 5 students.

# Create a Class named Rectangle which stores length and breadth of a rectangle. The class Should have method named aread & perimeter to calculate area and perimeter of the rectangle. 
class Rectangle:
    def __init__(self,lenth,breadth):
        self.lenth = lenth
        self.breadth = breadth
    def area(self):
        return self.lenth * self.breadth
    def perimeter(self):
        return 2 * (self.lenth + self.breadth)

lenth=int(input("Enter the Length of Rectangle:"))
breadth=int(input("Enter the Breadth of Rectangle:"))
obj = Rectangle(lenth,breadth)
print("Area of Rectangle:",obj.area())
print("Perimeter of Rectangle:",obj.perimeter())
    
class Student:
    def __init__(self,name,rollno,marks):
        self.name = name
        self.rollno = rollno
        self.marks = marks
    def total_marks(self):
        return sum(self.marks)
    def average_marks(self):
        return sum(self.marks)/len(self.marks)
students = []
for i in range(5):
    name = input("Enter Student Name:")
    rollno = input("Enter Roll Number:")
    marks = []
    for j in range(3):
        mark = float(input(f"Enter marks for subject {j+1}:"))
        marks.append(mark)
    student = Student(name, rollno, marks)
    students.append(student)
for student in students:
    print(f"Student Name: {student.name}, Roll Number: {student.rollno}, Total Marks: {student.total_marks()}, Average Marks: {student.average_marks()}")
    
    