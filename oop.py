# Python - Object Oriented Programming 

# 1. Create and Instantiating clases
# 2. Inheritance 
# 3. Class and Instance Variables
# 4. Static and Class methods

# Method : A function associated with a class 


# Create en employee class to fill all details 

class Employee: 

    def __init__(self,first,last,age,pay):



        #we can mention what other arguments we want to accept while creating instance of this class
        #set all of the instance variables

        self.first=first
        #this is similar to emp_1.first='Pramod'
        self.last=last
        self.age=age
        self.pay=pay
        self.email=first+'.'+last+'@gmail.com'

    # add methods to the class  
    def fullName(self):

        return ("{} {}" ).format(self.first,self.last)




    


# Class Vs Instance of a class

#instance variables contains data which is specific /unique to each instance 

#One way of doing things
# first , last , age,pay are all what ar eknown as attributes of the class 

emp_1=Employee('Pramod','Singh',33,35)
emp_2=Employee('Neha','Ziaan',31,10)

# print(emp_1)
# print(emp_2)


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
print(emp_1.fullName())
print(emp_1.email)
print(Employee.fullName(emp_1))



