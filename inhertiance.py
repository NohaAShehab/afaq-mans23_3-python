"1- intro to inheritance"

# class Person:
#     pass
#
#
# class Engineer(Person):
#     pass
#
#
#
# eng = Engineer()
# print(type(eng))
# print(isinstance(eng, Person))

"2- child inherits parent "
# class Person:
#     def __init__(self,name):
#         self.name= name
#         self._email = 'ddd'
#
#
#     def speak(self):
#         print(self.name)
#
# class Engineer(Person):
#     pass
#
#
#
# eng = Engineer("Ahmed")
# eng.speak()


""" both child and parent class have constructor ,__init__ ?"""

# class Person:
#     def __init__(self,name):
#         self.name= name
#         self._email = 'ddd'
#
#
#     def speak(self):
#         print(self.name)
#
# class Engineer(Person):
#     def __init__(self,name, sep):
#         # super().__init__(name)
#         super(Engineer, self).__init__(name)
#         self.sep = sep
#
#
#
# eng = Engineer("Ahmed",'ai')
# eng.speak()
#
#
#

""" polymorphism and inheritance 
    overloading 
    overriding 


"""




# class Person:
#     def __init__(self,name):
#         self.name= name
#         self._email = 'ddd'
#
#
#     # def speak(self):
#     #     print(self.name)
#
#     def speak(self, message:str = 'hiii'):
#         print(f"My name is {self.name}, {message}")
# class Engineer(Person):
#     def __init__(self,name, sep):
#         # super().__init__(name)
#         super(Engineer, self).__init__(name)
#         self.sep = sep
#
#
#     # overriding
#     def speak(self):
#         super().speak('hello world')
#         print(f"{self.sep}")
#
# eng = Engineer("Ahmed",'ai')
# # eng.speak("hiiii")
# eng.speak()




""" python and multiple inheritance

    PYTHON support multiple inheritance
"""


class Person:
    def __init__(self, name):
        self.name = name


class Teacher(Person):
    pass


class Engineer(Person):
    def __init__(self, fff):
        print('I am engineer')

#
class Instructor(Teacher, Engineer):
    pass


i = Instructor('noha')
print(isinstance(i, Engineer), isinstance(i, Teacher), isinstance(i, Person) )

#
#
#
#
#
#
#












