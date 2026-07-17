# Create a class (2-D vector) and use it to create another class representing a 3-D vector.
class TwoD_Vector:
    x = 2
    y = 3
    def showTwo_D(self):
        print(f"This is the Two D Vector Class where X: {self.x} and Y: {self.y}")
    
class ThreeD_Vector(TwoD_Vector):
    z = 4
    def showThree_D(self):
        print(f"This is the Three D Vector Class where X: {self.x} and Y: {self.y} and Z: {self.z}")


twoD = TwoD_Vector()
twoD.showTwo_D()

threeD = ThreeD_Vector()
threeD.showThree_D()
    