# for loop in python

variable = [1, 2, 3, 4, 5]
letters = ['m', 'a', 'n', 'a', 'k']
for item in variable:
    for letter in letters:
        print(item, letter)
    if item >= 1:
        break


for i in range(10):             # starts from 0 and prints upto 10(excluding)
    print(i)

for i in range(1,11):           # starts from 1 prints upto 11(excluding)
    print(i)

for index,start in enumerate(letters,0):
    print(start,index)
