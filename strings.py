# this is a single line comment in python...
'''
This is a multiline
 comment in python
'''
message = 'hello world'
message = message.replace('hello', 'python')       # replace strings with strings...
print(message)

multiline_strings = """When i was a kid
i used to watch doremon"""
print(multiline_strings)
print("the length of above is:", len(message))
# -----------------------------
message_2 = "manak_upadhyay"
print(message_2[0])
print(message_2[10])
print(message_2[5])
print("hey", message_2[5:])        # this is called slicing
print(message_2.upper());
print("MANAK UPADHYAY".lower());
#----------------
variable = "This is just a sentence which is not so cool"
print(variable.count('is'))        # counts the number of times a string or character is apperaring in the string...
print(variable.find('just'))         #finds the specified string- return its position...
# print(dir(variable))        # prints all the methods and functions that we can use with variable
# print(help(str))            # prints all the methods(with descriptions) that we can use with a string...
# print(help(str.capitalize()))       # prints the description of the method captilisze...

# word = "manak"
# print(word[::-1])                     # code to reverse a string in python...

word = 'manak'
print(help(str.count('')))
