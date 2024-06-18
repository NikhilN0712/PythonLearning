#allow duplicate values and cannot be modified

a = (1,2,3,4,5)
b = ("gitesh","kunal","nikhil","nikhil","nitin","nerkar")
c = (True,False,True,False)
d = (False,"nikhil",45,4)


print(len(b))
print(type(b))


#tuples methods
#print(b.count("nikhil"))
#print(b.index("nikhil"))
#print(a[2])

print(a[0:2])

for i in b:
    print(i)

#joined
z = a +b +c+d
print(z)
print(type(z))
