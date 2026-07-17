'''
Create a class ‘Employee’ and add salary and increment properties to it. Write a method
‘salaryAfterIncrement’ method with a @property decorator with a setter which changes
the value of increment based on the salary.
'''
class Employee:
    salary = 15000
    increment = 20
    @property
    def salaryAfterIncrement(self):
        return (self.salary + ((self.salary*self.increment)/100))
    @salaryAfterIncrement.setter
    def salaryAfterIncrement(self,value):
        self.increment = ((value - self.salary) / self.salary) * 100

employee = Employee()
print("Salary:",employee.salaryAfterIncrement)

employee.salaryAfterIncrement = 21000

print("Increment:",employee.increment)
print("New Salary:",employee.salaryAfterIncrement)