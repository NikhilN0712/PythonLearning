# local veriable means value inside the function
def demo():
    x = 2  # inside function
    print(x)


def demo1():
    print(x)


demo()
# demo1()

# gobal variables means value outside the function
x = 20


def demo2():
    print(x)


def demo3():
    print(x)


demo2()
demo3()


# global keyword
def demo():
    global x  # new is global function
    x = 10  # inside function
    print(x)


def demo1():
    print(x)


demo()
demo1()

