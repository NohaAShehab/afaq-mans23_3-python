

"most versatile datatype in python"

""" based sequence """

""" non primitive datatype ? -->"""
"1- define a list"
l = []
myl = list()
print(l, myl)
""" 2-list can hold different values from different datatype even another list"""
l = ["Ahmed", 'Ali', 'Mohamed', 44, True, None , "iti", [4,5,6,'test', 2023, False]]
print(l)
"3- get len of list"
print(len(l))

"4- you can access list elements using index --> starts from 0 "
print(l[4])
print(l[7][4])

"5- list is mutable "
l[4]= 'Updated'
print(l)

"6- append element to the list ---> to the end of the list "
l.append('iti')
print(l)

"7- insert element"
l.insert(4, 'inserted')
print(l)


"8- pop element in the list"

# popped_ele=l.pop()
# print(popped_ele)
# print(l)

"9- pop element at specific index "

popped_ele = l.pop(4)
print(popped_ele)
print(l)

"10- remove element  --> remove first occurrence of the element"
l.remove('iti')
print(l)


'11- list concat'
l1= ['python', 'django']
l2 = ['flask', 'postgres']
l3=  l1 + l2
print(l3)


'12- extend a list '
l1.extend(l2)
print(l1)
print(l2)

l1.clear()  # remove all elements from the list



'13-for loop over the list '

for item in l2:
    print(item)

'14- print item and its index ? '

print(enumerate(l2))

for index, item  in enumerate(l2):
    print(index, item)

"hint you use it with the string "

"""in operator ---> hint can be used with string """

print('flask' in l2)


'generate list of numbers '

myrange = range(4,10, 2)
print(myrange)
print(list(myrange))

'you can cast string to list and vice versa'
name = 'noha'
print(list(name))

message = 'You are very sleepy'
print(message.split(' '), type(message.split(' ')))

'sort list  ---> make sure that all the list items from the same type ? '

items = ['python', 'iti', 'Odoo','Ahmed', 'ali', 'noha' ]

items.sort()
print(items)



items.sort(reverse=True)
print(items)




items = ['python', 'iti',10, True, 'Odoo','Ahmed', 'ali', 'noha',100, 'abc', 939393 ]

items.reverse()
print(items)