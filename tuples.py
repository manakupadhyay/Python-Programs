# TUPLES IN PYTHON...

# lists are mutable and tuples are immutable(that is we cant modify tuples)


# to create an empty tuple
empty_tuple = ()
empty_tuple_2 = tuple()
print(empty_tuple)


tuple_1 = ('Computer Science', 'Math', 'Chemistry', 'Physics','Math')
print(tuple_1)
tuple_2 = tuple_1
print(tuple_2)
# tuple_1[0] = 'CS'  --> this is wrong as tuple cannot be changed..they are immuatble...

print(dir(tuple))   # --> dir -- it prints all the methods and attributes that we can use...

temp = [("manak", 10), ("upadhyay", 20)]       # a list of tuples...

print(tuple_1.count('Math'))

print(tuple_1.index('Chemistry'))
