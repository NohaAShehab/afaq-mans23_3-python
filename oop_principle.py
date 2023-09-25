"""

    1- encapsulation :
        class - -> way of encapsulation
        wrap content --> into one container
            --> limit accessibility ()

        --> object contain data (instance variable) and behaviour (instance method)

            --> access modifiers
                --> public
                --> protected
                --> private
    2- inheritance:
        --> is a relationship

    3- polymorphism:
        ==> function has many forms
        ---> overloading:
                --> many forms for the same function in the same container (class)
                function sumnum(int num1, int num2)
                function sumnum(int num1)
                function sumnum(str num1)

        ---> overriding
            ---> must be in inheritance relation
            the same function with the same appears in the parent and the child class but different in function body

    4- abstraction
        ---> hide details
        ---> define abstract structure

        --> can be extended later




"""

""" encapsulation """


class Employee:
    def __init__(self, id, name, salary):
        self.id = id
        self.name = name
        self.salary = salary

    def printInfo(self):
        print(f'name = {self.name}')


#
# emp = Employee(1, 'ahmed' , 10000)
# print(emp)
# emp.printInfo()
# emp.id = 10
# print(emp.id)


""" python and access modifiers
    --> no  explict access modifiers 
    000> access modifiers --> determined according to variable name 
    
    public ---> start a-zA-z
    protected ---> start with _
    private ---> start with __
"""


# class Employee:
#     def __init__(self, id, name, salary):
#         self.id = id
#         self._name = name
#         self.__salary = salary
#
#     def printInfo(self):
#         print(f'name = {self._name}')
#
#
# emp = Employee(1, 'ahmed', 10000)
# print(emp.id)
# emp.id = 10
# print(emp.id)
#
# 'protected'
# print(emp._name)  # ethically don't do that
# emp._name= 'test'
#
# 'private'
# # print(emp.__salary)  #AttributeError: 'Employee' object has no attribute '__salary'
#
# # emp.__salary = 90000
#
# print(emp._Employee__salary)
#
# emp._Employee__salary=7389278947


""" setters and getters
    apply specific on properties 
 """
# class Employee:
#     def __init__(self, id, name, salary):
#         self.id = id
#         self._name = name
#         self.__salary = salary
#
#     def printInfo(self):
#         print(f'name = {self._name}')
#
#     def setSalary(self, sal):
#         if isinstance(sal, int) or isinstance(sal, float):
#             self.__salary = sal
#         else:
#             raise ValueError('salary should be int or float')
#
#     def getSalary(self):
#         return self.__salary*.8
#
#
# emp = Employee(1, 'ahmed', 10000)
#
# print(emp.getSalary())
# emp.setSalary("4499944")





""" property decorator """
# class Employee:
#     def __init__(self, id, name, salary):
#         self.id = id
#         self._name = name
#         self.__salary = salary
#
#     def printInfo(self):
#         print(f'name = {self._name}')
#
#     def setSalary(self, sal):
#         if isinstance(sal, int) or isinstance(sal, float):
#             self.__salary = sal
#         else:
#             raise ValueError('salary should be int or float')
#
#     def getSalary(self):
#         return self.__salary*.8
#
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
# emp = Employee(1, 'ahmed', 10000)
# # print(emp.salary())
# print(emp.salary)
#
# emp.salary = 7000000

" check this "
# class Employee:
#     def __init__(self, id, name, salary):
#         self.id = id
#         self._name = name
#         if isinstance(salary, int) or isinstance(salary, float):
#             self.__salary = salary
#         else:
#             raise ValueError('salary should be int or float')
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
# emp = Employee(1, 'ahmed', 'iti')
# emp.printInfo()
# print(emp.salary)

"""best practice """
class Employee:
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

    @property
    def age(self):
        return 10

emp = Employee(1, 'ahmed', 10000)
emp.printInfo()
print(emp.salary)
print(emp.age)

emp.age= 25


#lab --> apply inheritance