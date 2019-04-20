# Python - Object Oriented Programming 

# 1. Create and Instantiating clases
# 2. Inheritance 
# 3. Class and Instance Variables
# 4. Static and Class methods

# Method : A function associated with a class 


# Create en employee class to fill all details 

class Employee: 
    #Class variables
    raise_amount=1.04
    num_of_emps=0

    def __init__(self,first,last,age,pay):

        

        #we can mention what other arguments we want to accept while creating instance of this class
        #set all of the instance variables

        self.first=first
        #this is similar to emp_1.first='Pramod'
        self.last=last
        self.age=age
        self.pay=pay
        #self.email=first+'.'+last+'@gmail.com'

        Employee.num_of_emps +=1

    # add methods to the class  
    def fullName(self):

        return ("{} {}" ).format(self.first,self.last)

    

    def apply_raise(self):
        self.pay=int(self.pay*self.raise_amount)

    #add class method 

    @classmethod
    def set_raise_amount(cls,amount):
        cls.raise_amount=amount
    #alternative constructors 
    @classmethod

    def from_string(cls,emp_string):
       first,last,age,pay=emp_string.split("-")
       return cls(first,last,age,pay)

    #static method

    @staticmethod
    def is_workday(day):
        if day.weekday()==5 or day.weekday()==6:
            return False
        else:
            return True
    
    #sepcial methods 
    def __repr__(self):
        return "Employee ('{}' ,'{}','{}','{}')".format(self.first,self.last,self.age,self.pay)

    def __str__(self):
        return "{},{}".format(self.fullName(),self.email)

    def __add__(self,other):

        return self.pay + other.pay

    def __len__(self):

        return len(self.fullName())

    #decorator
    Keep using method as an attribute 
    @property
    def email(self):
        return "{}.{}@gmail.com".format(self.first,self.last)


    
            



    


# Class Vs Instance of a class

#instance variables contains data which is specific /unique to each instance 

#One way of doing things
# first , last , age,pay are all what ar eknown as attributes of the class 

emp_1=Employee('Pramod','Singh',33,35)
emp_2=Employee('Neha','Ziaan',31,10)

print(repr(emp_1))
print(str(emp_1))
print(emp_1+ emp_2)
print(len(emp_1))
print(emp_1.email)


#create instance variable manually

# emp_1.first='Pramod'
# emp_1.last='Singh'
# emp_1.email='pramod.chahar@gmail.com'
# emp_1.pay=10000


# emp_2.first='Neha'
# emp_2.last='Za'
# emp_2.email='neha.za@gmail.com'
# emp_2.pay=1000

# print(emp_1.email)
# print(emp_2.email)

#but its not actually making use of a class instead we define a special method ( __init__ method ) ,Its an initialization method or constructor 
#when we create methods within the class ,they recieve the instance(self) as the first argument automatically.You can call that anything apart from self but by convention 'its called 'self')

#Notice we need a parenthesis here as its a method not an attribute
# print(emp_1.fullName())
# print(emp_1.email)
# print(Employee.fullName(emp_1))

# print(emp_1.pay)
# emp_1.apply_raise()
# print(emp_1.pay)
#namespace
# print(emp_1.__dict__)
#print(Employee.__dict__)
# print(Employee.num_of_emps)

# Employee.set_raise_amount(1.80)
# emp_1.set_raise_amount(12.05)

# print(Employee.raise_amount)
# print(emp_1.raise_amount)
# print(emp_2.raise_amount)

# emp_3=Employee.from_string('Ziaan-chaudhary-3-66')

# print(emp_3.email)

# print(Employee.num_of_emps)

# import datetime

# my_date=datetime.date(2016,7,10)

# print(Employee.is_workday(my_date))

# Inheritance

class Developer(Employee):

    raise_amount=1.50

    def __init__(self,first,last,age,pay,language):
        #let main class handle default arguments

        #super().__init__(first,last,age,pay)
        Employee.__init__(self,first,last,age,pay)

        self.language=language


    # To add addtional attributes to the subclass , we need to declare init method specific to sublcass 

    
    
    

    


class Manager(Employee):

    def __init__(self,first,last,age,pay,employees=None):
        #let main class handle default arguments

        #super().__init__(first,last,age,pay)
        Employee.__init__(self,first,last,age,pay)

        if employees==None:
            self.employees=[]
        else:
            self.employees=employees

    def add_employee(self,emp):
        if emp not in self.employees:
            self.employees.append(emp)
    
    def del_employee(self,emp):
        if emp  in self.employees:
            self.employees.remove(emp)

    def print_emp(self):
        for emp in self.employees:
            print('---->',emp.fullName())

    
#print(help(Developer))


# dev_1=Developer('chenna','P',33,5000,'tableau')
# dev_2=Developer('surya','krishna',30,3000,'python')
# #Chnage in the attribute in subclass , it doesnot effect on the main Employee class

# # print(dev_1.pay)
# # dev_1.apply_raise()
# # print(dev_1.pay)
# print(dev_1.language)

# mngr_1=Manager('Vijay','Agnee',50,500000,[dev_1])

# mngr_1.add_employee(dev_2)
# print(mngr_1.print_emp())