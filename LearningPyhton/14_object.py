class person:

    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    def fullname(self):
        return f"{self.fname}{self.lname}"


a = person("nikhil", "nerkar")
b = person("kunal", "nitin")

c = a.fullname()
print(c)


class information:
    def __init__(self, name, age, location):
        self.name = name
        self.age = age
        self.location = location

    def format(self):
        return self.name + " " + str(self.age) + " " + self.location


a = information("nikhil", 12, "mahim")
b = information("kunal", 12, "nitin")

c = a.format(), b.format()
print(c)


