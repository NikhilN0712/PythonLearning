x = "my name is nikhil"
y = "my name is nikhil and last name is nerkar"

print(x[1])
print(y)
print("is" in x)


#string functions
#len(),  str(), upper(), count(), upper(), lower(), split(), find(), ,replace(), strip() = is remove spaces and caracter

x= "nikhil nerkar"
y= 9867279069

print(len(x))

z = str(y)
print(z.find("69"))

print(x.upper())

print(x.count("n",0,5))

print(x.split())

print(x.replace("nikhil","sneha"))


#string sliceings

a = " hello my name is nikhil and i live in mahim"

print(a[1:6])
print(a[1:6:2])
print(a[-3])
print(a[-7:-3])
print(a[:])


#string formating
x = "nikhil"
y = "mahim"

print("hello "+x+" in " +y) #1

print("hello %s in %s" % (x, y)) #2 or change vlue
print("hello %s in %s" % ("patker", y))

print("hello {1} in {0}".format(x, y)) #3 or
print("hello {name} in {location}".format(name=x, location=y))


