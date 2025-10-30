# class
class Calculator:
    def add(self, x, y):
        print(f"The sum of {x} and {y} is {x + y}")
    def subtract(self, x, y):
        return x - y
    def multiply(self, x, y):
        return x * y
    def float_divide(self, x, y):
        return x / y

obj = Calculator()
obj.add(5, 3)
sub = obj.subtract(10, 4)
print(f"The difference is {sub}")
mul = obj.multiply(2, 6)
print(f"The product is {mul}")
float_div = obj.float_divide(8, 2)
print(f"The float division result is {float_div}")


# inheritance
class Person:
    def _init_(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(f"Name: {self.name}, Age: {self.age}")
class Student(Person):
    def first(self):
        print("i am a student")
    

obj1 = Person("Alice", 30)
obj1.display()

obj2 = Student("Bob", 20)
obj2.display()
obj2.first()