
"""

    block of code --> perform task -->
    write it once ---> use many time

"""

'''functions syntax '''


'1- define a function '


# def myfun():
#     pass
#
# print(type(myfun))
#
#
# '2- call function'
# res= myfun()
# print(res)

''' define function'''
# def myfun():
#     return
#
# print(type(myfun))
#
#
# '2- call function'
# res= myfun()
# print(res)
#

# def sayhello():
#     print('hello world')
#
# res =sayhello()
# print(res)

' function accept arguments '

################### functions with mandatory number of arguments #################
def sumnum (num1, num2):
    print(f"num1={num1}, num2={num2}")
    print(num1 +num2)
    return

# res=sumnum(20,330)
# print(res)

# res=sumnum(20,330, 33,333)  #TypeError
# print(res)

# sumnum(29,303)
#
# sumnum('33','3333')

'''function that returns with results'''
# def calculator(num1, num2, nuum3):
#     res =  num1 + num2 + nuum3
#     return  res
#
# r= calculator(10,20,30)
# print(r)
""" function return with multiple values 000> tuple"""
# def calculator(num1, num2, nuum3):
#     res =  num1 + num2 + nuum3
#     return  res, num1, num2

# r= calculator(10,20,30)
# print(r)

# m= calculator(20,30)


"""----------------------------------------------------------"""

# functions with optional arguments

# def sumnum(num1, num2=10):
#     print(f"num1={num1}, num2={num2}")
#     res = num1 + num2
#     print(res)
#
#
# sumnum(30 ,33)
#
# sumnum(333)

''' problems of functions '''

# def sumnum(num1, num2):
#     res = num1 +  num2
#     print(res)
#     return  res
#
# r= sumnum(10 , 203)
# m = sumnum('Ahmed', 'ali')


'specify datatypes of the arguments '
# def sumnum(num1:int, num2:int):
#     res = num1 +  num2
#     print(res)
#     return  res
#
# r= sumnum(10 , 203)
# m = sumnum('Ahmed', 'ali')
#

print(isinstance('iti', int))
#
# def sumnum(num1:int, num2:int):
#     if isinstance(num1, int) and isinstance(num2, int):
#         res = num1 +  num2
#         print(res)
#         return  res
#
# r= sumnum(10 , 203)
# m = sumnum('Ahmed', 'ali')
# s =sumnum(444,'555')
# #


""" functions with unknown number of arguments """
#
# print('noha', 'ahmed', 'ali')
# print('mohamed')
#

def activestudents(*students):  # * ---> zero or more --> regex --> regular expressions
    print(students)

#
# activestudents('Ahmed', 'khaled', 'mohamed', 'ali')
#
# print('ahmed', 'noha', sep='|||', end='     ')
# print('iti')
# print('fff')



""" functions with keyword arguments """

def askforinfo(**info):  # ** function arguments --> key=value
    print(info) # dict

askforinfo(name='noha', age=31, works_at='iti')
askforinfo(fname='mohamed', lname='ahmed')
askforinfo()


info = "my name is {username}"
print(info.format(username='noha'))




