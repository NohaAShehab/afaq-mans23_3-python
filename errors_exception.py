

"""

    errors :
        syntax error : parser --> solve it -->

        logical error --> developer

        runtime error

"""


# def sumnum(num1, num2):
#     return  num1 * num2
#
# print(sumnum(2,2))
#
# print(sumnum(3,4))
# ## unit tests for your application



""" ==========> runtime error """
print('--- hello world ---')
# print(name) # runtime error , exception


# num = int(input('please enter number: '))
# print(num)


#
# print(5/0)  # ZeroDivisionError


##################################  Exception handling ##################################

# try:
#     # print(name)
#     num  = int(input('please enter number: '))
# except:
#     print('--- problem happened')
#
# print('--------- after the block ---------------')



""" exception state """

#
# try:
#     # print(name)
#     # num  = int(input('please enter number: '))
#     print(3/0)
# except Exception as e:
#     print(f'--- problem happened ---> {e}' )
#
# print('--------- after the block ---------------')




# try:
#     print(name)
#     num  = int(input('please enter number: '))
#     print(3/0)
# except NameError as ne:
#     print(f"{ne} --> you should restart the app and redecalre it ")
# except ValueError as ve:
#     print(f"{ve} --> you should enter integer value not string  ")
# except ZeroDivisionError as ze:
#     print(f"Division by zero is not allowed")
# except Exception as e:
#     print(f'--- problem happened ---> {e}' )
#
# print('--------- after the block ---------------')


# try:
#     num = int(input('please  enter number: '))
# except NameError as ne:
#     print(f"{ne} --> you should restart the app and redecalre it ")
# except ValueError as ve:
#     print(f"{ve} --> you should enter integer value not string  ")
# except ZeroDivisionError as ze:
#     print(f"Division by zero is not allowed")
# except Exception as e:
#     print(f'--- problem happened ---> {e}' )
# else:
#     print(num)
#
# finally:
#     print('--- this block will be executed always ')
# print('--------- after the block ---------------')




# def askfornum():
#     try:
#         num = int(input('please enter number '))
#     except Exception as e:
#         print(e)
#         return False
#     else:
#         return  num
#     finally:
#         ## the code in this block --> executed before return
#         print("------- function executed successfully -----")
#
# res = askfornum()
# print(res)

####################### Raising the exception ################################


def sumnum(num1:int, num2:int):
    if not isinstance(num1, int) or not isinstance(num2, int):
        raise TypeError('num1 and num2 must be integers ')
    return  num1 + num2

# print(sumnum('2',3))

# print(max('ww',44))

















