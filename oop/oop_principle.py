"""

    oop ?

"""

emp = {
    "id": 1,
    "name": "ahmed",
    'sal': 1000
}

emp2 = {
    "empid": 1,
    "emp_name": "ahmed",
    'emp_sal': 1000
}

# defined user customized datatype
# class --> class blue for user-defined datatype

"1- create class"
# class Employee:
#     pass
#
# "2- take object from the class"
#
# e = Employee()
# print(e, type(e))

# l=[]
# print(type(l))

# if e:
#     print('hii')
# else:
#     print('bye')

"""3- add properties to the object """
# e.name  = 'ahmed'
# e.id = 10
# e.salary = 1000
#
# print(e.name)
#
#
# e2= Employee()
# e2.empname='noha'
# e2.id= 11
# e2.sal = 1000


"""4-customize object creation """

# class Employee:
#
#     def __init__(self):  # constructor function --> called while creating object
#         print(f'------- new object is being created now  ------- {self}')
#         # id,name, sal - --> properties  --- instance variables
#         self.id = 1
#         self.name='noha'
#         self.salary=1000
#
# e = Employee()
# print(e)
# e2= Employee()

"""customize object creation, instance method """
# class Employee:
#
#     def __init__(self, id , name, salary):  # constructor function --> called while creating object
#         self.id = id
#         self.name=name
#         self.salary=salary
#
#     def printEmpInfo(self):  # instance method =--> output depends on the caller instance
#         print(f'Emp = {self.name}, {self.id}, {self.salary}')
#
# e = Employee(1, 'ahmed', 2000)
# print(e)
# e2= Employee(2,'noha', 2999)
# e.country ='Egypt'
#
# e.printEmpInfo()
# e2.printEmpInfo()

"""-------------------------Class Variable ----------------------------------------------------"""
""" ---------> count no of objects """
# class Employee:
#     count = 0  # class variable  # shared property between all instances of the class
#
#     def __init__(self, id , name, salary):  # constructor function --> called while creating object
#         self.id = id
#         self.name=name
#         self.salary=salary
#         # self.__class__.count +=1
#         Employee.count +=1
#
#     def printEmpInfo(self):  # instance method =--> output depends on the caller instance
#         print(f'Emp = {self.name}, {self.id}, {self.salary}')
#
#
# print(Employee.count)
# e = Employee(1, 'ahmed', 2000)
# print(e)
# e2= Employee(2,'noha', 2999)
#
# print(e2.count)
#
# e.printEmpInfo()
# e2.printEmpInfo()
#
# print(f'No. of objects = {Employee.count}')
#
#
# Employee.country= 'Egypt'
#
"""--------------------------- Class Method -------------------------------------------"""




# class Employee:
#     count = 0  # class variable  # shared property between all instances of the class
#
#     def __init__(self, id , name, salary):  # constructor function --> called while creating object
#         self.id = id
#         self.name=name
#         self.salary=salary
#         # self.__class__.count +=1
#         Employee.count +=1
#
#
#     def printEmpInfo(self):  # instance method =--> output depends on the caller instance
#         print(f'Emp = {self.name}, {self.id}, {self.salary}')
#
#     @classmethod  # the first parameter of the function --> represent the class
#     def get_no_of_employees(cls):
#         print(cls)
#         print(cls.count)
#
#     @classmethod  # acts like object factory
#     def create_emp(cls):
#         return  cls(1, 'fff', 33333)
#
#
# Employee.get_no_of_employees()
# e = Employee(1, 'ee', 2222)
# e.get_no_of_employees()
#
# m = Employee.create_emp()
#
# e2 = Employee(3, 'ee', 2222)
# e.get_no_of_employees()
#
# print(Employee.count)





"""----------------------------- Static methods ---------------------------------------"""


class Employee:
    count = 0  # class variable  # shared property between all instances of the class

    def __init__(self, id , name, salary):  # constructor function --> called while creating object
        self.id = id
        self.name=name
        self.salary=salary
        # self.__class__.count +=1
        Employee.count +=1


    def printEmpInfo(self):  # instance method =--> output depends on the caller instance
        print(f'Emp = {self.name}, {self.id}, {self.salary}')

    @classmethod  # the first parameter of the function --> represent the class
    def get_no_of_employees(cls):
        print(cls)
        print(cls.count)

    @classmethod  # acts like object factory
    def create_emp(cls):
        return  cls(1, 'fff', 33333)

    @staticmethod
    def calnetSalary(salary):
        return salary * .8


Employee.get_no_of_employees()
e = Employee(1, 'ee', 2222)

print(e.calnetSalary(e.salary))

print(Employee.calnetSalary(894789))


def calnetSalary(salary):
    return salary*.8


print(calnetSalary(e.salary))


print(calnetSalary(200000))















