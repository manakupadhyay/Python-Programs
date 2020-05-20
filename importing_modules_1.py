
print("this is module 1")

test = "this is just a string"


def my_function(list, target):
    for i, value in enumerate(list):
        if(value == target):
            return i
    return -1
