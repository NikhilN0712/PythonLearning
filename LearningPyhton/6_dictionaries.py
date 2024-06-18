
a = {1:10, 2:20, 3:30, 4:40}
b = {"a":1, "b":2, "c":3, "d":4}

print(a[1])
#add
b["nikhil"]="7"
print(b)

#remove
b.pop("nikhil")
print(b)

#dictionaries methods
#get(), keys(), items(), values(), pop(), popitem(), update(), copy(), clear()

c = {"nikhil":1,"patkar":2,"kunal":3,"gitesh":4}
#return only values
print(c.get("gitesh"))

#return in lists on keys
print(c.keys())

#return all values
print(c.items())

#return all values
print(c.values())

#remove items
print(c.pop("nikhil"))

#remove last kay and values
print(c.popitem())

#add or update values
c.update({"nitin":5})
print(c)

#copy dic
d = c.copy()
print(d)


