# Can you change the self-parameter inside a class to something else (say “harry”)? Try
# changing self to “slf” or “harry” and see the effects.
class Test:
    name = "Eshwar Lal"
    def getInformation(slf):
        print("My name is:",slf.name)

test = Test()
test.getInformation()

# Yes! we can replace self with any name (like slf). It works the same way.