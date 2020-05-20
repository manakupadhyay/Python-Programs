# LISTS IN PYTHON


# to create an empty list
empty_list = []
empty_list_2 = list()

# ----------

languages = ['C++', 'Java', 'JavaScript', 'Python',8]
# print(min(languages))
print(languages)
print(languages[2])     # print the second index
print(languages[0:3])   # print from 0(inclusive) to 3(exclusive)
print(languages[1:])        # print everything starting from 1 to the end of the list
print(languages.index('Java'))      # return the index of specified item if found, else error...
print('JavaS' in languages)      # returns true if specified value is in list, else returns false...

languages.append('C')   # appends the item to the last
print(languages)
languages.insert(0, 'HTML')      # insert(location, value)
print(languages)

frameworks = ['Django','Flask']
# languages.insert(0,frameworks)       it will generate a list within list...
# languages.append(frameworks)         it will append the specified list with the new list(list within list)...
languages.extend(frameworks)        # it will not make a list within list...
print(languages)

languages.remove('Flask')
print(languages)

popped = languages.pop()        # it return and deletes the last value in the list...
print(popped)
print(languages)
languages.sort(reverse=True) # sorts the list in descending order...
# languages.reverse()         # reverses the list...
print(languages)

languages.sort()            # sorts the list in alphabetical order

numbers_list = [2, 10, 4, -6, 18, 11, 5]
print(numbers_list[-1])     # -1 when used with lists return the last item...
# numbers_list.sort() -- sorts the list is ascending order...
print(numbers_list)

numbers_list_sorted = sorted(numbers_list)      # it return the sorted version of the list specfied
print(numbers_list_sorted)

print(min(numbers_list_sorted))     # returns the minimum number in the list....
print(max(numbers_list_sorted))     # returns the maximum number in the list...
print(sum(numbers_list_sorted))     # returns the sum of the list...


# for loops with lists...

laptops = ['Dell', 'HP', 'Lenevo', 'Apple']
for index, value in enumerate(laptops, start=1):
    print(index, value)


# lists and strings...
string = ' - '.join(laptops)
print(string)
print(type(string))

new_list = string.split(' - ')
print(new_list)
