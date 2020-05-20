# DICTONARIES IN PYTHON...

# dictonaries are basically key-value pairs (like hashmap in c++)

# to create an empty dictonary...
empty_dictonary = {}
empty_dictonary_2 = dict()
# ---------------

me = {'Name': 'Manak Upadhyay', 'Age': '19', 'fav_car': 'Audi', 'Subjects': ['Computer Science', 'Maths', 'Chemistry']}
print(me)
print(me['fav_car'])
print(me.get('Address', ' Found'))       # get method return the specified argument if the mentioned key is not found...
me['Name'] = 'Manak'            # it will update the name key...
me['Address'] = 'Noida'         # it will add the new key with its value...
print(me)



me.update({'Name': 'Manak Upadhyay', 'Phone': '555-55555'})         # it will update in one shot...
print(me)

# removing elements...

del me['fav_car']
print(me)

phone = me.pop('Phone')
print(me)
print(phone)
# ---------------------------
print(len(me))          # prints the length of the dictonary
print(me.keys())        # print all the keys in the dictonary
print(me.values())      # prints all the values in the dictonary
print(me.items())       # prints all the keys-value pairs...

# using for loops in dictonary

for keys, value in me.items():
    print(keys, value)
