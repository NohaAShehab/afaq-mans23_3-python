
''' any .py file is a python module

    --> you can import this module in other module or part of it
'''
# def validateNum(num):
#     if isinstance(num, int) or isinstance(num, float):
#         return True
#
#
# def calculator(num1, num2):
#     if validateNum(num1) and validateNum(num2):
#         return  num1 + num2
#
# print(calculator(3,345))


'''import all the module content  '''

# import  validation

# def calculator(num1, num2):
#     if validation.validateNum(num1) and validation.validateNum(num2):
#         return  num1 + num2
#
# print(calculator(3 ,345))
#
#
# print(validation.validaName('ahmed   '))


'''import part of the module ? '''

#
# from validation import  validaName
#
# print(validaName('noha'))

''' Alias the module name, functions'''

# import  validation as v
#
# print(v.validateNum(1000))

#
# from validation import  validateNum as vm
# print(vm(44444))

####### get function from package ?

''' import packagename.modulename '''

# import  iti.python_inputs
#
# print(iti.python_inputs.askforInt('please enter age: '))

# import  iti.python_inputs as myin
#
# print(myin.askforInt('please enter age: '))


'''import part of the module from the package '''
#
# from iti.python_inputs import  askforInt
#
# print(askforInt('please enter salary'))


# import summertraining


# import  summertraining.greeting
# summertraining.greeting.sayhello('hello')


import  summertraining

summertraining.sayhello('Ahmed')



