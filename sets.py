"""
    lists
    tuple
    set

    set ---> doesn't allow data duplication --> it is only allow immutable datatype
        ---> unordered datatype
        ---> no index for the items

"""

"1- define a set "

s = set()

"2- set can hold different data from different datatypes"
myset = {'Ahmed', 'Ali', 22, 'iti', 'iti', 44.4, True, None}
print(myset)

" set is mutable  unordered datatype "

"3- add element to specific position"
myset.add('new element')
print(myset)

'4- get len of the set'
print(len(myset))

'5- check if the element exists in the set ... '
print('iti' in myset)

'6- pop element from the set ---> randomly'
popped_element = myset.pop()
print(popped_element)
print(myset)

"7- remove element from the set "
# you check if the element exists or not in this set.
myset.remove('iti')
print(myset)

'8- update the set '

myset1 = {
    "django", 'flask', 'postgres'
}

myset.update(myset1)
print(myset)


'add tuple, set to a set'

# ss = {'Ahmed', True, ('python', 'flask')}
# print(ss)

ss = {'Ahmed', True, ['python', 'flask']}
print(ss)


""" set store only hashable datatype  =immutable= """

# set --> cannot any mutable datatype





















