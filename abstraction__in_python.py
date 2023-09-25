
"""

    abstraction based on the inheritance

"""
# ABC --> abstract base class
from abc import  ABC, abstractmethod


"to define abstract class"



# class Person(ABC):
#     pass
#
# # this is not an abstract class
# p=  Person()


""" abstract class must contains at least one abstract method. """
"""
    abstraction
        --> general reusable architecture 
"""
class Person(ABC):

    @abstractmethod
    def speak(self):
        pass


# p=  Person()

class Employee(Person):
    def speak(self):
        pass


emp = Employee()


