''' scoping --> accessibility level of the variable in the script'''


######### global scope ##################
'''any variable defined in the python script --> has scope => global scope '''
# course = 'python'
# print(course)

##### local scope ########
''' any variable defined inside any function --> local variable scope '''
''' local variable can be accessed only inside the function '''
# def sayhello():
#     name= input('please enter name : ')
#     print(f'Hello {name}'.title())
#
# sayhello()
# print(name)

#### access global variable inside the function

course ='python'

## read the value
def printCourse():
    print(f"course = {course}".title())

printCourse()


### modify course value ?

# def modifycourse():
#     course = input('please enter course value: ')  # generate new local variable
#     print(f"course= {course}".title())
#
#
# modifycourse()
# print(course)

# def modifycourse():
#     global  course
#     course = input('please enter course value: ')  # new assign
#     print(f"course= {course}".title())
#
#
# modifycourse()
# print(course)
#
#
# name='khaled'
# name = 'ahmed' # new assignment


############### function inside a function



# def outerfunction():
#     course ='Django'  # local variable
#     # can be accessed anywhere in the function
#
#     def innerfunction():
#         print(course)
#
#     innerfunction()
#     print(f'course = {course}')



# def outerfunction():
#     course ='Django'  # local variable
#     # can be accessed anywhere in the function
#
#     def modifycourse():
#         course = input('please enter coursename : ')  # new local variable for the inner function
#         print(course)
#
#     modifycourse()
#     print(f'course = {course}')
#
# outerfunction()

""" modify local variable of the parent function"""

def outerfunction():
    course ='Django'  # local variable
    # can be accessed anywhere in the function

    def modifycourse():
        nonlocal course
        course = input('please enter coursename : ')  # new local variable for the inner function
        print(course)

    modifycourse()
    print(f'course = {course}')

outerfunction()



