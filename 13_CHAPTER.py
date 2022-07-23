#VIRTUAL ENVIROMENT: An enviroment which is same as the system interpretor but is isolated from the other python enviorments on the system.

#ACTIVATING AND DEACTIVATING VIRTUAL ENVIROMENT:

#PS D:\PYTHON COURSE> .\firstvirtualenv\Scripts\activate.ps1
# (firstvirtualenv) PS D:\PYTHON COURSE> deactivate
# PS D:\PYTHON COURSE>

# "pip freeze" will give you the list of packages installed along with there versions.
# "pip freeze > requirements.txt" will copy the list to a text file.
# "pip install -r .\requirement.txt" will install all the pacakges present in the given file.

#LAMBDA FUNCTION: A type of conveniance which allows us to defina a function in single line.

#this is the simple method without using lambda keyword:
def func(a):
    return a+5
x= 566
print(func(x))

#this is how we can define a function using a lambda keyword:
func= lambda a: a+5
x= 566
print(func(x))

#Another Example function defination using Lambda Keyword:

func =lambda a: a+5
square = lambda x: x*x
sum = lambda a,b,c:a+b+c

x= 3
print(func(x))
print(square(x))
print(sum(x,1,2))

# JOIN METHODS: Returns all the elements in a Iterable datatype in the form of sentance (string) having a specific keyword between them.

l= ["hello","welcome","to","world","of","Virtuality"]
a= " and ".join(l)
print(a)
print(type(a)) # will print the datatype of "a"

# FORMAT METHODS (strings) : formats the values inside the string into a desired output. same as "f" string but it is used in ancient computing when "f" string is not introduced.
#e.g
name = "Alex"
about = "virtual machine"

a= "This is {0},a {1} to help you out.".format(name, about) # 0 and 1 represent the location of argument
print(a)

# MAP Method:
#e.g
def square (num):
    return num *num 

l = [1,2,4]

# Method 1: simple method
l2=[]
for item in l:
    l2.append(square(item))
print(l2)

# Method 2: by using map keyword:
print(list(map(square, l))) #this will map the list into the function.

# FILTER Method: creates a list for which the function returns True.
#e.g

def greater_than_5(num):
    if num >5:
        return True
    else:
        return False

l =[1,2,3,4,45,5]
print(list(filter(greater_than_5, l))) #will filter the list according to the function.


#REDUCE Method: Applies a rolling computaion to sequence pair of elements
from functools import reduce

sum = lambda a,b: a+b

l = [1,2,3,4] 
val = reduce(sum, l)
print(val) # val = 10

#CHAPTER 13 PRACTICE SET:

#Que_1 Create two virtual enviroments, install few packages n the first one. how do you create a simiar enviroment in the second one?

'''Created using terminal and some of the commands given below:
   pip freeze,deactivate,.\env2\Scripts\activate.ps1 and few more.'''

#QUE_2 Wrie a program to input name,marks and phone number of a student and format it using the format function like below:
#"The name of the student is Marry,her marks are 72 and phone number is 999999999"

name = input("Enter your name: ")
marks = int(input("Enter your marks: "))
phone = int(input("Enter your phone number: "))

temp ="The Name of the student is {}, his marks are {} and phone number is {}"
output = temp.format(name,marks,phone)
print(output)

#Que_3 A list contains the multiplication table of 7.Write a program to convert it to a vertical string of same numbers.

l = [str(i*7) for i in range(1,11)]
print(l)
# using join function
verticleTable = "\n".join(l)
print(verticleTable)

#Que_4 Write a program to filter a list of numbers which are divisible by 5

l = [34,66,775,55,654,345,55,34,553,770]
a= filter(lambda a: a%5 == 0, l)
print("Filtered Elements: ", list(a))

#Que_5 Write a program to find the maximum of the numbers in a list using the reduce function.

l= [1,33,45,666,55,66]
val = reduce(max, l)
print(val)

#Que_6 Explore the Fash module and create a web server using Flask and Python.

from flask import Flask #Flask is a Framework developed in python to build web servers and websites.
app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Hello, World!"

if __name__=="__main__":
    app.run(debug=True)

# AUTHOR : RRO-SHAN
# LOCATION : EARTH 286
# DATE : 17TH OF DECEMBER 2021 
# TIME : 08:21 AM IST