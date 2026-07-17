# Override the __len__() method on vector of problem 5 to display the dimension of the
# vector.
class Vector:
    def __init__(self, values):
        self.values = values

    def __add__(self, other):
        result = []

        for i in range(len(self.values)):
            result.append(self.values[i] + other.values[i])

        return Vector(result)

    def __mul__(self, other):
        result = 0

        for i in range(len(self.values)):
            result += self.values[i] * other.values[i]

        return result
    def __len__(self):
        return len(self.values)
    def __str__(self):
        return str(self.values)


v1 = Vector([2, 3, 4])
v2 = Vector([5, 6, 7])

print("Addition:", v1 + v2)
print("Dot Product:", v1 * v2)
print("Dimension of Vector:",len(v1))