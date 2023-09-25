""" special methods  """

# class Employee:
#     def __init__(self, id, name, salary):
#         self.id = id
#         self._name = name
#         self.salary = salary  # this will call the property setter
#
#     def printInfo(self):
#         print(f'name = {self._name}')
#     @property
#     def salary(self):
#         return self.__salary * .8
#
#     @salary.setter
#     def salary(self, sal):
#         if isinstance(sal, int) or isinstance(sal, float):
#             self.__salary = sal
#         else:
#             raise ValueError('salary should be int or float')
#
#     def __str__(self):
#         "must retrun with string  --> calling when you try to print the object "
#         return f"{self._name}"
#
#
#     def __repr__(self):
#         return f'Employee(id={self.id},name={self._name}, salary={self.salary})'
#
#     def __len__(self):
#         return len(self.__dict__)
#
#
#     def __call__(self):
#         print("---- object called ------")
#
#
# emp = Employee(10, 'ahmed', 8983947)
# print(emp)
# print(emp.__repr__())
#
# print(emp.__dict__)  # representation object in form dict
#
# print(len([4,4,4,4,4]))
#
# emp.nddd = 'ddddd'
# print(len(emp))
#
#
# emp()

""" check this """


class Employee:
    __slots__ = ('id', '_name', '__salary')

    def __init__(self, id, name, salary):
        self.id = id
        self._name = name
        self.salary = salary  # this will call the property setter

    def printInfo(self):
        print(f'name = {self._name}')

    @property
    def salary(self):
        return self.__salary * .8

    @salary.setter
    def salary(self, sal):
        if isinstance(sal, int) or isinstance(sal, float):
            self.__salary = sal
        else:
            raise ValueError('salary should be int or float')

    def __str__(self):
        "must retrun with string  --> calling when you try to print the object "
        return f"{self._name}"

    def __repr__(self):
        return f'Employee(id={self.id},name={self._name}, salary={self.salary})'

    def __len__(self):
        return 3

    def __call__(self):
        print("---- object called ------")


emp = Employee(10, 'ahmed', 8983947)
print(emp)
print(emp.__repr__())
#
# print(emp.__dict__)  # representation object in form dict
#
#
# emp.nddd = 'ddddd'
# print(len(emp))
#
# emp()


# del Employee.__slots__