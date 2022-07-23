# INHERITANCE AND MORE ON OOPs : Inheritance is a way of creating a new class from an existing class.

#e.g of single Inheritance

class Employee:                              #PARENT CLASS
    company = "Google"
       
    def showDetails(self):
        print("This is an employee")

class Programmer(Employee):                  #DERIVED CLASS = Continue of the parent class.
    
    language = "Python"
    company = "Microsoft"                                 #This will be overwrited.
    
    def getLanguage(self):
        print(f"The language is {self.language}")
    
    def showDetails(self):
        print("This are the modified details by the child class.") #This will be overwrited.

e= Employee()
e.showDetails()
p = Programmer()
p.showDetails()
print(p.company)
 

#Types of Inheritance

'''
1. Single Inheritance : occurs when child class inherits only a single parent class.
2. Multiple Inheritance : occurs when child class inherits from more than one parent classes.
3. Multilevel Inheritance : occurs when child class keep on inherits form thier consecutive parent classes.
'''

#e.g of Multiple Inheritance:

class Employee:            #Parent Class 1
    company = "CurlFit"
    eCode = 120

class Freelancer:           #Parent Class 2
    company = "Fiverr"
    level = 0

class Programmer(Employee, Freelancer): # Child Class
    name = "David"

p = Programmer
print(p.eCode)
print(p.level)
print(p.company) # Will print parent1 class's company.

#e.g of Multilevel Inheritance:

class Person:
    country = "INDIA"

    def takeBreath(self):
        print("I am Breathing....")

class Employee(Person):
    company = "Honda"

    def salaryInfo(self):
        print(f"Salary is {self.salary}")

    def takeBreath(self):
        print("I am an employee and I am breathing....")

class Programmer(Employee):
    company = "Microsoft"

    def salaryInfo(self):
        print(f"No salary to programmer.")

p = Person()
p.takeBreath()
e = Employee()
e.takeBreath()
pr = Programmer()
pr.takeBreath() # will use the nearest parent.

# Super methods: used to access the method of a super class in the derived class.
#e.g

class Person:
    country = "INDIA"

    def takeBreath(self):
        print("I am Breathing....")

class Employee(Person):
    company = "Honda"

    def salaryInfo(self):
        print(f"Salary is {self.salary}")

    def takeBreath(self):
        super().takeBreath() # WILL ALSO PRINT THE PARENT METHOD.
        print("I am an employee and I am breathing....")
        
class Programmer(Employee):
    company = "Microsoft"

    def salaryInfo(self):
        print(f"No salary to programmer.")

p = Person()
p.takeBreath()
e = Employee()
e.takeBreath()
pr = Programmer()
pr.takeBreath()

# Class Methods: A method which is bounded to a class.

class Employee:
    company = "Tesla Inc."
    salary = 10000000
    location = "California, USA"

    def changeSalary(self, sal):
        self.salary = sal

e = Employee()
print(e.salary)
e.changeSalary(40000000) # will create a new instance attribute of salary and equate it with the new value.It will not change class attribute.
print(e.salary) # will change but,
print(Employee.salary) #this will not change due to the above mentioned process.

# To change class Method, we can use the following method.

class Employee:
    company = "Tesla Inc."
    salary = 10000000
    location = "California, USA"

    @classmethod   #Decorator
    def changeSalary(cls, sal): #changing class attributes value.
        cls.salary = sal

e = Employee()
print(e.salary)
e.changeSalary(40000000) #now this will change the class attribute's value.
print(e.salary)  #now the value of this and below written statement will be same as class attribute's value has been change.
print(Employee.salary)

# Property of Decorator:

#e.g When the company bonous keep on changing

class Employee:
    company = "Nuralink"
    salary = 5600
    salaryBonus = 400

    @property #It will be a function but works kind a property of a class for us.
    def totalSalary(self):
        return self.salary + self.salaryBonus
    
    @totalSalary.setter #It will SET the bonus according to the given total salary by reducing it with fixed amount of salary.It is a function but works a s a property for the user.
    def totalSalary(self,val):
        self.salaryBonus = val - self.salary

e = Employee()
print(e.totalSalary)
e.totalSalary = 5800
print(e.salary)
print(e.salaryBonus)

# Operators Overloading in python : operators in pyhton can be oveloaded using dunder methods. These method are called when a given operator is used on the objects.
#e.g 

class Number:
    def __init__(self, num): 
        self.num = num

    def __add__(self, num2): #add dunder add numbers,
        print("Let's add")
        return self.num + num2.num

    def __mul__(self, num2): #mul dunder to multiply numbers.
        print("Let's multiply")
        return self.num * num2.num

n1 = Number(4)
n2 = Number(6)
sum = n1 + n2
mul = n1 * n2
print(sum)
print(mul)

#other dunder/magic method in pyhton:
#e.g

class Number:
    
    def __init__(self, num): 
        self.num = num

    def __str__(self): # Str dunder method we can print what's in a object.
        return f"Decimal Number: {self.num}"

    def __len__ (self): #len dunder method by which we can set length of a object.
        return 1

n1 = Number(9)
print(n1)
print(len(n1))

# CHAPTER_11 PRACTICE SET:
#QUE_1 Create a class C2d Vector and use it to create another class resprenting a C3-d vector.

class C2dVector: #Parent class
    def __init__(self, i, j):
        self.icap = i
        self.jcap = j
    
    def __str__(self):
        return f"{self.icap}i +{self.jcap}j"
        
class C3dVector(C2dVector): #Child class
    def __init__(self, i, j , k):
        super().__init__(i, j)
        self.kcap = k

    def __str__(self):
        return f"{self.icap}i +{self.jcap}j +{self.kcap}k"

v2d = C2dVector(1,3)
v3d = C3dVector(1,3,5)
print(v2d)
print(v3d)

#QUE_2 Create a class pets from a class Animals and further create class Dog from Pets.Add a method "bark" to class dogs.

class Animals:
    AnimalType = "Both wild and pets"

class Pets(Animals):
    catagory = "Pets"

class Dogs(Pets):
    @staticmethod
    def Bark():
        print("BHOW!! BHOW!!")
        
d = Dogs
d.Bark()

#QUE_3 Create a calss employee and add salary and increment properties to it. Write a method "salaryAfterIncrement" method with a @property decorator with a setter which changes the value of increment based on the salary.

class Employee:
    salary = 1000
    increment = 1.5
 
    @property
    def salaryAfterIncrement(self):
        return self.salary*self.increment

    @salaryAfterIncrement.setter
    def salaryAfterIncrement(self, salint):
        self.increment = salint/self.salary

e = Employee()
print(e.salaryAfterIncrement)
print(e.increment)
e.salaryAfterIncrement = 2000 #new value will be stored and incremnt will be printed accordingly.
print(e.increment)

#QUE_4 Write a class Complex to represent complex to represent complex numbers, along with overload operator + and * which add and multiplies them.

class Complex():
    def __init__(self, r, i):
        self.real = r
        self.imaganary = i

    def __add__(self, c):
        return Complex(self.real +c.real, self.imaganary +c.imaganary)
    
    def __mul__(self, c):
        mulReal = self.real*c.real - self.imaganary*c.imaganary
        mulImg = self.real*c.imaganary + self.imaganary*c.real
        return Complex(mulReal,mulImg)

    def __str__(self):
        return f"{self.real}+{self.imaganary}i"


c1 = Complex(2,8)
c2 = Complex(9,6)
print(c1+c2)
print(c1*c2)

#QUE_5 Write a class vector represnting a vector of "n" dimension. Over the + and * operator which alculates the sum and the dot product of them.

class vector:
    def __init__(self, vec):
        self.vec = vec

    def __str__(self):
        str1 = ""
        index = 0
        for i in self.vec:
            str1 += f" {i} a{index} +"
            index +=1
        return str1[:-1]
    
    def __add__(self, vec2):
        newList = []
        for i in range(len(self.vec)):
            newList.append(self.vec[i] +vec2.vec[i])
        return vector(newList)

    def __mul__(self, vec2):
        sum = 0
        for i in range(len(self.vec)):
            sum += self.vec[i] * vec2.vec[i]
        return sum

v1= vector([1,4,6])
v2 = vector([1,6,9])
print(v1+v2)
print(v1*v2)

#QUE_6 Write "str" method to print the vector as follows: 7i+8j+10k

class vector:
    def __init__(self, vec):
        self.vec = vec
    
    def __str__(self):
        return f"{self.vec[0]}i + {self.vec[1]}j +{self.vec[2]}k" 

v = vector([7,8,10])
print(v)

#QUE_7 Overwrite the len() method on vector of problem 5 to display the dimention of the vector.

class vector:
    def __init__(self, vec):
        self.vec = vec

    def __str__(self):
        str1 = ""
        index = 0
        for i in self.vec:
            str1 += f" {i} a{index} +"
            index +=1
        return str1[:-1]
    
    def __add__(self, vec2):
        newList = []
        for i in range(len(self.vec)):
            newList.append(self.vec[i] +vec2.vec[i])
        return vector(newList)

    def __mul__(self, vec2):
        sum = 0
        for i in range(len(self.vec)):
            sum += self.vec[i] * vec2.vec[i]
        return sum

    def __len__(self):       #Adding len method
        return len(self.vec)

v1= vector([1,4,6])
v2 = vector([1,6,9])
print(len(v1))               #printing the length of vectors
print(len(v2))

#Assingment: print "Programm Failure" when the length of two vectors are not equal.

# AUTHOR : RRO-SHAN
# LOCATION : EARTH 286
# DATE : 31TH OF OCTOBER 2021 
# TIME : 10:55 PM IST