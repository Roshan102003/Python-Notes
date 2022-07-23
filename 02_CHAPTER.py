#ASSIGNING VARIOUS DATA TYPES TO A VARIABLE

a= "hello world" # eg. of string. 
b= 83839 # eg. of integer.
c= 45.32 # eg. of floating point number.
print(a)
print(b)
print(c)

d= False # eg. of Booleans
e= None  # used to represent Nothing.
print(d)
print(e)

#PRINTING THE TYPE OF VARIABLE.
print(type(a)) #gives datatype of a variable
print(type(b))
print(type(c))
print(type(d))

#RULES TO ASSIGN NAMES TO VARIABLES
''' 1.CAN'T START FROM A SPECIAL CHARACTER OR DIGIT
    2.CAN'T HAVE SPACES BETWEEN NAMES
    3.CAN'T HAVE THE NAME OF A KEYWORD
    4.CAN ONLY START WITH UNDERSCORE AND ALPHABETS'''

#OPERATORS IN PYTHON
  
   #Arthimetic operator
a=3
b=4
print("The value of 3+4 is:", 3+4) 
print("The value of 3-4 is:", 3-4)
print("The value of 3*4 is:", 3*4)
print("The value of 3%4 is:", 3%4)

   # Assignment operators
c = 34
c -= 12
c *= 12
c /= 12
print(c)

   #Comparison Operators
d = 14>4
print(d)
d = 7>14
print(d)
   
   #Logocal Operators
bool1 = True
bool2 = False

print("The value of bool1 and bool2 is",(bool1 and bool2))
print("The value of bool1 or bool2 is",(bool1 or bool2))
print("The value of not bool2 is",(not bool2))
print("The value of not bool1 is",(not bool1))

#Converstion of data type of variable:
''' int : try to covert the datatype into integer
    float : try to covert the datatype into decimal
    str :try to covert datatype into string'''


#PRACTICE SET CHAPTER_2

#QU1_1
y=3
z=5
print("Sum of these two number is", y+z)

#QUE_2
x= 45
w= 5
print("The remainder when x is divided by w is", x%w)

#QUE_3
a=34
b=54
print(a>b)

#QUE_4
m=5
n=8
print("The average of these number will be :", (m+n)/2)

#QUE_3
k=4
print("The square of the given number will be", k*k)


# AUTHOR : RRO-SHAN
# LOCATION : EARTH 286
# DATE : 5TH OF OCTOBER 2021 
# TIME : 7:30 PM IST