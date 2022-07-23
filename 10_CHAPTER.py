#OBJECT ORIENTED PROGRAMMING :Solving a problem using a object.
#Follows "DRYS" PRINCIPAL.

#e.g. of procedural oriented programming.
a= 4
b= 45
print("Sum of the two number is:",a+b)

#e.g. of object oriented programming.
class Number:
    def sum(self):
        return self.a + self.b

num= Number() # object Instantiation
num.a= 4
num.b= 45
s= num.sum()
print(s)
          
# CLASS: Blueprint of creating a object in python.
'''
     Blank form ----->Filled by candidate------>Application
lly  CLASS ---------->Object instatiation------>OBJECT

'''               
#We write class in pascal case.Class consist of some variable and methods.

#Cases in Python:
'''
PascalCase
EmployeeName------>PascalCase

CamelCase
isNumeric, isFloatOrInt ------>Camel Case

'''

# Object :Instantiation of a class is called an Onject in python.

#e.g_1 Railways
class RailwayForm:
    formType = "RailwayForm"
    def printData(self):
        print(f"Name is {self.name}")
        print(f"Train is in {self.train}")

samApplication = RailwayForm()
samApplication.name = "Sam"
samApplication.train = "NewYork Subway"
samApplication.printData()

#e.g_2 Game Pad
class remote:
    def right(self): #IMPLEMENTATION DETAILS
        pass
    def left(self):
        pass
    def top(self):
        pass
    def down(self):
        pass

class Player:
    def moveRight(self): #IMPLEMENTATION DETAILS
        pass
    def moveLeft(self):
        pass
    def moveTop(self):
        pass
    def moveDown(self):
        pass

player_1 = Player()
remote_1 = remote()

if(remote_1.left()):
    player_1.moveLeft()

# NOTE: Object of a given class can invoke the methods avaliable to it without revealing the implementation details to the user.
# NOTE: Classes sre just like Modules in python

# MODELLING IN OOPs

'''

Noun -----------> Class -----------> Employee
Adjective ------> Attributes ------> name,age,salary
Verb -----------> Methods ---------> getSalary(),increment()

'''
#Class Attributes: Attribute belonging to class rather than a particular object.
#e.g:

class Employee:
    Company = "Google"       # Specific to each class

sam = Employee()             # Object instantation
jerry = Employee()
print(sam.Company)
print(jerry.Company)

Employee.Company = "Youtube" # Changing class Attribute
print(sam.Company)
print(jerry.Company)

#Instance Attributes: Attributes belonging to the Instance(Object) of an object. 
#e.g

class Employee:
    Company = "Google"      
    salary = 100

sam = Employee()             
jerry = Employee()
sam.salary = 300
jerry.salary = 400

print(sam.salary)          #will show instance attribute as instance attribute overpower the class attribute.
print(jerry.salary)

#NOTE: Instance attribute take preference over the class attributess during assingment and retrival:
# 1. Is attribute is present in object?
# 2. Is attribute is present in class?
#e.g

class Employee:
    Company = "Google"      
    salary = 100

sam = Employee()            
jerry = Employee()

#Creating instance attribute salary for both the objects
#sam.salary = 300
#jerry.salary = 400

print(sam.salary)        #will show class attribute when instance attribute is not present.
print(jerry.salary)

#Self() Parameter: Prarmeter which passes through a object itself.
#e.g

class Employee:
    Company = "Amazon"
    def getSalary(self):
        print("Salary is 100k")

peter = Employee()
peter.getSalary() #<--------Self internally coverts this into the below written statement internally and output will be generated accordingly.
                  #Employee.getSalary(peter) the advanntage is we can use various attributes and class of the object now. here self is "peter".

# Static Method: When we didn't want to pass an object to a function, we use "@staticmethod".It basically that function that doesn't need a self parameter.
#e.g

class Employee:
    Company = "Amazon"
    
    @staticmethod         #A Decorator to mark greet as a static method.
    def greet():
        print("Welcome to Amazon India")

peter = Employee()
peter.greet()

#Functions and Methods are same. Variables, Attributes, Properties are the same in OOPs. 

#___int___() Constructor : ___int___() is a special method which is first run as soon as the object is created. this method is also known as constructor.It take self argument as well as other araguments.
#e.g

class Employee:
    Company = "Amazon"

    def __init__(self,name,salary,subunit):           #Runs itself.
        self.name = name
        self.salary = salary
        self.subunit = subunit
        print("Employee has been created!")
    
    def getdetails(self):
        print(f"The name of the Employee is {self.name}")
        print(f"The salary of the Employee is {self.salary}")
        print(f"The subunit of the Employee is {self.subunit}")

peter = Employee("Sam",100000,"Youtube") #printed by first function by constructor method.
peter.getdetails()                       #printed by second function.

#PRACTICE SET CHAPTER_10
#QUE_1: Create a class programmer for storing information of few programmers working at microsoft.

class programmer:
    company = "Microsoft"
    
    def __init__(self, Name, Product):
        self.name = Name
        self.product = Product
    def getInfo(self):
        print(f"The name of the programmer is {self.name} and the the product is {self.product} under {self.company}.")

Carter = programmer("Carter", "Skype")
Mike = programmer("Mike", "GitHub")

Carter.getInfo()
Mike.getInfo()

#QUE_2 Write a class calculator capable of finding square,cube and square root of a number.

class calculator:
    def __init__(self,num):
        self.num = num

    def square(self):
        print(f"The value of {self.num} square is {self.num**2} ")
    def squareroot(self):
        print(f"The value of {self.num} squareroot is {self.num**0.5}")
    def cube(self):
        print(f"The value of {self.num} cube is {self.num**3}")

a = calculator(3)
a.square()
a.squareroot()
a.cube()

#QUE_3 Create a class with a class attribute a ; create an object from it and set a directly using object a=0. Does this change the class attribute?

class sample:
    a = "sample class Attribute"

obj = sample()
obj.a = "modified class Attribute"
print(obj.a)

#Ans.No because we have only changed the attribute of a object not the class.

#QUE_4 Add a static method in problem 2 to greet the user.

class calculator:
    def __init__(self,num):
        self.num = num
    @staticmethod
    def greet():
        print("Welcome to the Calculator.")
    def square(self):
        print(f"The value of {self.num} square is {self.num**2} ")
    def squareroot(self):
        print(f"The value of {self.num} squareroot is {self.num**0.5}")
    def cube(self):
        print(f"The value of {self.num} cube is {self.num**3}")

a = calculator(3)
a.greet()
a.square()
a.squareroot()
a.cube()

#QUE_5 Write a class Train which has methods to book a ticket, get status(no. of seats) and get fare information of train running under Indian Railways.

class Train:
    Authority = "Mars variance Authority"
    
    @staticmethod
    def greet():
        print("Welcome to Mars Variance Authority")
    
    def __init__(self, name, fare, seats):
        self.name = name
        self.fare = fare 
        self.seats = seats
    
    def getStatus(self):
        print(f"The name of the train is {self.name}")
        print(f"The seats in the train are {self.seats}")
    
    def fairInfo(self):
        print(f"The fare of the Train is: Rs. {self.fare}")
    
    def bookTicket(self):
        if(self.seats>0):
            print(f"Your ticket has been Booked! Your seat number is {self.seats}")
            self.seats = self.seats - 1
        else:
            print("Sorry, all the seats has been booked kindly try for next season.")

Intersteller = Train("Intersteller Express: 2070", 90, 300)
Intersteller.greet()
Intersteller.getStatus()
Intersteller.fairInfo()
Intersteller.bookTicket()

#QUE_6 Can you cahnge the self paprameter inside a class to something else (say "slf"). Try changing self to "slf" and see the effect.

class change():
    
    def initial(self):
        print("This is a sample of unmodified self.")
    def final(self):
        print("This is a modified self to 'slf'.")

random = change()
random.initial()
random.final()

#Ans. Yes, it works, but it is not recommende because it will reduce code readablity.

# AUTHOR : RRO-SHAN
# LOCATION : EARTH 286
# DATE : 29TH OF OCTOBER 2021 
# TIME : 6:25 PM IST