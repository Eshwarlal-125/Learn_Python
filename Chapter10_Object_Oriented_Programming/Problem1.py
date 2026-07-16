# Create a class “Programmer” for storing information of few programmers working at Microsoft.
class Programmer:
    company = "Microsoft"

    def __init__(self,name,empid,salary):
        self.name = name
        self.employeeId = empid
        self.salary = salary
        print("This is the Information of Employee!")

Waseem = Programmer("Waseem Tunio",2,300000)
print("Name:",Waseem.name,"| Employee_ID:",Waseem.employeeId,"| Salary:",Waseem.salary,"| Company:",Waseem.company)