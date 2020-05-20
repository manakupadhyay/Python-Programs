'''sum of elements of a list... '''
ele = int(input('Enter the number of elements: '))
i = 1
list = []
add = 0
while i <= ele:
    num = int(input('enter number: '))
    list.append(num)
    add = add + list[i-1]
    i = i + 1
print("sum is: ", sum(list))


'''factorial of a number'''
# num = int(input("enter the number: "))
# fact = 1
# while num > 0:
#     fact = fact * num
#     num -= 1
#
# print("factorial is: ", fact)


'''multiplication table of a number'''


# num = int(input("enter the number: "))
# i = 1
# for i in range(1,11):
# print(str(num) + ' * ' + str(i) + ' = ' + str(num * i))
