# SETS IN PYTHON..

# sets are values that are unordered and don't have duplicates...


# to create an empty list

empty_dictonary = set()
print(empty_dictonary)

set_1 = {'Noida', 'New Delhi', 'Gurugram', 'Greater Noida'}
var = 'Noida'
print(var in set_1)

print(set_1)        # they print values in random order...

set_2 = {'Noida', "Banglore", 'Pune', 'Hyderabad','Noida'}
print(set_2)

print(set_2.intersection(set_1))        # prints the intersection of set_2 and set_1
print(set_2.difference(set_1))          # prints all those courses that are in set_2 but not in set_1
print(set_2.union(set_1))               # prints the union of both the sets...

print(dir(set_1))

set_1.remove('Noida')
print(set_1)

set_1.clear()
print(set_1)
