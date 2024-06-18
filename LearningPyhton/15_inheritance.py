# class p_class:
# def __init__(self):
# print("parent class instance")

# def p_mathod(self):
# print("parent money")

# class c_class(p_class):
# pass

# c = c_class()
# c.p_mathod()

class information:
    location = "tdyjrc"

    def __init__(self, name, age, ):
        self.name = name
        self.age = age

    def format(self):
        print(self.name + " " + str(self.age) + " " + self.location)


class student(information):
    location = "ewrwer"


a = student("ndsf", 12)
a.format()

