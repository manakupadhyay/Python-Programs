
from importing_modules_1 import my_function as f1, test as t

#import sys                  # this is the module that contains the list of directories from where we can import
                            # modules successfully

# import importing_module_1
# import importing_module_1 as im1(this will be an alias for importing_module_1)
# from importing_module_1 import my_function (for this we will not have to use dot and module name)
# from importing_module_1 import my_function as f1(here f1 is an alias for my_function)

courses = ['math', 'computer science', 'chemistry', 'physics']

index = f1(courses, 'chemistry')

print(index)
print(t)

# print(sys.path)
