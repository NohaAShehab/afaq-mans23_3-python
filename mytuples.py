

"most versatile datatype in python"
# 
""" based sequence """
# 
""" non primitive datatype ? -->"""
"1- define a tuple"
t = ()
myt = tuple()
print(t, myt)
""" 2-tuple can hold different values from different datatype even another tuple"""
t= ("Ahmed", 'Ali', 'Mohamed', 44, True, None , "iti", (4,5,6,'test', 2023, False))
print(t)
"3- get len of tuple"
print(len(t))
# 
# "4- you can access tuple elements using index --> starts from 0 "
print(t[4])
print(t[7][4])

# "5- tuple is immutable "
# t[4]= 'Updated'
# print(t)


# 

# 
# 


# 

# '11- tuple concat'
t1= ('python', 'django')
t2 = ('flask', 'postgres')
t3=  t1 + t2
print(t3)
# 
# 

# 
#
# 

'13-for loop over the tuple '

for item in t2:
    print(item)
# 
# '14- print item and its index ? '
# 
#
for index, item  in enumerate(t2):
    print(index, item)
# 
# "hint you use it with the string "
# 
# """in operator ---> hint can be used with string """
# 
print('flask' in t2)
# 
# 
# 'generate tuple of numbers '
# 
myrange = range(4,10, 2)
print(myrange)
print(tuple(myrange))

# 'you can cast string to tuple and vice versa'
name = 'noha'
print(tuple(name))
# 


'tuple of one item'

mytt = ('iti',)
print(mytt)