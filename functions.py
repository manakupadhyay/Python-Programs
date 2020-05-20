# FUNCTIONS IN PYTHON...


def function():
    print("hello functions")
    return 10

def function_1():                       # this is just declaration/prototype of function...
    pass

print(function)
print(function())
print(function_1())


def function_1():
    return 20

print(function_1())



# def is_even(num):
#     num = int(num)
#     if num % 2 == 0:
#         print("number is even")
#     else:
#         print("number is odd")
#
#
# number = input("enter any number: ")
# is_even(number)

def just_a_function(par1, par2, par3="Hey", par4="hello"):
    print("par 1 is:", par1)
    print("par 2 is", par2)
    print("par 3 is", par3)
    print("par 4 is", par4)


just_a_function(2, 3, par4='hi')


def check_reference(a, b):
    a += 2
    b += 1


num1 = int(input("enter first number: "))
num2 = int(input("enter second number: "))
print("num1 is", num1)
print("num2 is", num2)
check_reference(num1, num2)
print("num1 is", num1)
print("num2 is", num2)
