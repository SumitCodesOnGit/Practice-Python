# Oops practice session

# Student management system

# base class
class Person:

    def __init__(self,name,age):
        self.name = name   # public attribute
        self._age = age     #  protected attribute


    def show_details(self):
        print(f"Name: {self.name}, Age: {self.age}")


# Derived class (inheritance)
class Student(Person):
    def __init__(self,name,age,student_id):
        super().__init__(name,age)
        self.__student_id = student_id  # private attribute

    def show_details(self):     # polymorphism
        print(f"Student Name: {self.name}, ID: {self.__student_id}")

    def get_id(self):
        return self.__student_id   # accessor for private attribute
    

# Another derived class (inheritance)
class Teacher(Person):

    def __init__(self,name,age,subject):
        super().__init__(name,age)
        self.subject = subject

    def show_details(self):    # polymorphism
        print(f"Teacher Name: {self.name}, Teaches: {self.subject}")


# Test the OOP system
s1 = Student("Sumit",27,"R0003")
t1 = Teacher("Mr Sunny", 37, "Electronics")

people = [s1,t1]

for person in people:
    person.show_details()   # polymorphic beahviour

# accessing private data safely
print("Student ID:", s1.get_id())

""" Concept Practiced:
Class and Object | Student("Sumit",27,"R0003")
Encapsulation | _age (protected) and __student_id(private)
Inheritance | Student and Teacher inehrit Person
Polymorphism | show_details() behaves differently per class
Accessor | get_id() safely exposes private data
"""
        

        

