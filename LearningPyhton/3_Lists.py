x = 10
y= "nikhil"
a=[12,34,23,54]
b = ["nikhil",23,45,"patkar"]

print(a[3])
print(type(b))
print(b[1:2])

#list methods
#append(), remove(), pop(), index(), count(), insert(), sort(), reverse(), copy(), clear()

cities = ["mumbai", "Dhlil","kolkata","goa","up"]

cities.append("mp")
print(cities)

cities.insert(1,"nepal")
print(cities)

cities.remove("up")
print(cities)

cities.pop(5)
print(cities)

print(cities.index("Dhlil"))

print(cities.count("mumbai"))

cities.sort()
print(cities)

cities.reverse()
print(cities)

new = cities.copy()
print(new)

new.clear()