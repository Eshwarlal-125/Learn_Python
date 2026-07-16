# Add a static method in problem 2, to greet the user with hello.
class Calculator:
    number = 4
    def sqaure(self):
        return self.number*self.number
    def cube(self):
        return self.number*self.number*self.number
    def sqaure_root(self):
        if(self.number < 0):
            return "Give Valid Number > 0"
        return self.number**0.5
    @staticmethod
    def greet(name):
        print("Hello!",name)

number = Calculator()
print("Number: ",number.number)
print("Square of a Number: ",number.sqaure())
print("Cube of a Number: ",number.cube())
print("Square Root of a Number: ",number.sqaure_root())
number.greet("Eshwar")

    