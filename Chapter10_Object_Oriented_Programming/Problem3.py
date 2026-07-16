# Create a class with a class attribute a; create an object from it and set ‘a’
# directly using ‘object.a = 0’. Does this change the class attribute?

class Main:
    a = 10

object = Main()
object.a = 0

print(object.a)
print(Main.a)

# No! it does not change the class attribute. It only creates/changes the attribute for that specific object.