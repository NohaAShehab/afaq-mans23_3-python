
"comma seperated key value pair datatype "

'1- to define the dict '
d = {}   # empty dict
myd = dict()

'2- hold key:value pair --> comma '
myinfo = ['noha', 'mansoura']  # unlabeled data
info = {  # labeled data
    "name": 'noha',
    'city': 'cairo',
    'name': "Noha Shehab"
}

print(info)
"dict doesn't allow key duplication"

'3- you access values of the dict using key '
print(info['name'])

'4- dict is mutable datatype '

info['name']= 'Noha AbdelHady Shehab'
print(info)

info['work']= 'iti'
print(info)

'from 3.7 --> dict --> ordered datatype '

'5- pop element from the dict'

# popped_value=info.pop('work')
# print(popped_value)

'6- delete key:value '
# del info['name']
# print(info)

'7-check if element exists in the dict '
print(info)
print('cairo' in info)  # in --> check if value exists in the keys

'8- get keys of dict ?'

keys = info.keys()  # dict_keys --> you can cast it to  a list
print(keys, type(keys))

keys_list = list(keys)
print(keys_list)


'8- get values of dict ?'

values = info.values()  # dict_values --> you can cast it to  a list
print(values, type(values))

keys_values = list(values)
print(keys_values)

print('cairo' in info.values())

'9- loop over the dict '

for item in info:
    print(f"{item} : {info[item]}" )

'10- update dict '

add_info = {"salary":1000, 'track':'opensource', 'city':'Zayed'}

info.update(add_info)
print(info)

'11- get len of dict '
print(len(add_info))

'12- get items of the dict '

print(info.items()) # dict

items = info.items()
items = list(items)
print(items)

for key, value in items:
    print(f"{key}:{value}")


'13- clear dict '
info.clear()
print(info)