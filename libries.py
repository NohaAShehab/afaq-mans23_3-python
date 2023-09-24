import os

print(os.getcwd())

# print(os.mkdir('test'))
#
# print(os.getlogin())
#
# import math
# print(math.pi)
#
# math.pi ='ffff'
#
# print(math.pi)


""" regular expression """
import re

pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'

email = input('please enter email: ')

res = re.match(pattern, email)   # return with match object if the part of the string follow pattern
print(res)

res = re.fullmatch(pattern, email)   # return with match object if the part of the string follow pattern
print(res)