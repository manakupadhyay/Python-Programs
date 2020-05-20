
# if, else, elif
# there are no switch statements in python...

a = 10
if a == 10:
    print("a is 10")
elif a == 20:
    print("a is 20")
else:
    print("a is shit")

list = [1,2,3,4]
list_2 = [1,2,3,4]
list_3 = list

if list == list_2:                      # == compares the content of the two objects
    print("both are same")
else:
    print("different")

print(id(list))                 # prints the memory location of the variables (like pointers in c++)
print(id(list_2))
print(id(list_3))

print(list is list_3)           # is compares whether the objects point to same memory in memory, if yes it gives
print(list is list_2)                            # true otherwise false...


name = 'manak'
boolean = False

if name == 'manak' and boolean:                 # and operator
    print("case 1")
elif name == 'manak' and not boolean :          # not operator
    print('case 2')
elif name == 'upadhyay' or not boolean:         # or operator
    print('case 3')
else:
    print('not case matched')


# False Values in python:
    # False
    # None
    # Zero of any numeric type
    # Any empty sequence. For example, '', (), [].
    # Any empty mapping. For example, {}.

condition = None

if condition:
    print('Evaluated to True')
else:
    print('Evaluated to False')