
# from 'file' import 'class'
from Student import Student     # check Student file how a class is defined
from datetime import date
from Person import Person

# Check Employee file on how it has been inherited from Person
from Employee import Employee

student_1 = Student("Ravi", "Computers", 3.2, False)
print(student_1.name)
print(student_1.display_student())

person_1 = Person("Sankar", date(1987, 9, 26))
print(person_1.show_occupation())
print(person_1.calculateAge())

employee_1 = Employee("Ravi", date(1991, 9, 26))
print(employee_1.show_occupation())
print(employee_1.calculateAge())