# Write a class “Calculator” capable of finding square, cube and square root of a number.
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

number = Calculator()
print("Number: ",number.number)
print("Square of a Number: ",number.sqaure())
print("Cube of a Number: ",number.cube())
print("Square Root of a Number: ",number.sqaure_root())

    