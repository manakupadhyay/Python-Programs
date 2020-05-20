# EXCEPTIONS IN PYTHON

dividend = int(input('Enter the dividend: '))
divisor = int(input("Enter the divisor: "))

try:                                            # whatever we want to examine for exception goes here...
    ans = dividend/ divisor
    # raise Exception
except Exception as x:                          # if an exception occurs, control comes here...
    print("Exception is: ", x)
else:
    print("answer is: ", ans)                   # if no exception is raised, else block is executed
finally:
    print("this is finally block")              # finally block is always executed...

