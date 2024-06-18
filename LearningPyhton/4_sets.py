# set remove dubalicat values
set_0 = {10, 20, 30, 30, 50, 40, 50}
set_1 = {40, 50, 60, "nikhil"}
set_2 = {"nikhil", "nerkar", "patkar", "gitesh"}
set_4 = set((10, 20, 30, 40, 50))

print(set_0)
print(set_4)

# set method
# add(), remove(), discard() or pop(), clear()

a = {"mumbai", "dhlhi", "kolkata", "goa"}
b = {"mumbai", "dhlhi", "kolkata", "goa", "up", "mp"}

a.add("mahim")
print(a)

a.remove("mahim")
print(a)

a.pop()
print(a)

# joining two methods
# union() or update()

c = a.union(b)
print(c)

d = a.update(b)
print(d)

# keep only dublicates
# intersection() or intersection_update()

e = a.intersection(b)
print(e)

e = a.intersection_update(b)
print(e)

# remove dublicates vlues
# symetric_difference or symetric_difference_update
f = a.symmetric_difference(b)
print(f)

f = a.symmetric_difference_update(b)
print(f)

# remove dublicates vlues print unique values
# difference or difference_update

g = a.difference(b)
print(g)

g = a.difference_update(b)
print(g)