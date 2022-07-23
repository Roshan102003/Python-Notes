# FUNCRTIONS: Group of statements used to perform specific tasks.

#eg. This is how we can define a function

def percent(marks): #Here we have defined a function and now we can call any number of time in our code.
    return((sum(marks)/500)*100) #Function Defination.

marks_1 = [3,3,3,3,3] #We have given the input.
percentage_1 = percent(marks_1) #We have send the value to the function.
print(percentage_1) #After going through the function value will be printed-Function calling.

#Quick_Quiz: Write a program to greet a user with "Good Day" using functions.
def greet(name):
    print("Have a Good Day " + name)

greet('Eternals.') # Here we call the function first time.
greet("Aliens.") #Here we call the function second time.

#Types of Functions in Python:

''' 1. Built in function : Function which are already present in pyhton. eg. print(),len() etc.
    2. User defined Function : Function defined by user, like we defined a function named greet() the previous program.'''

# Function with Argument:
'''The input which we put in a function or the input on which the function operates is called Argument.'''

#Default Parameter Value:

def greet(name = "Stranger"): #here "Stranger" works as a default parameter argument.
    print("Good Day " + name)

greet("Pal.") # Here the parameter will change and output will be generated.
greet() # Python will not show any error because the intial value of greet will sustained and output will be generated.

# Recursion: Function which calls itself. Used to directly use a mathematical formula as a function.

def factorail_iter(num): # Factorial using for loop.
    product = 1
    
    for i in range(num):
        product = product * (i+1)
    return product
 
print(factorail_iter(5))
    
#n! = 1*2*3*3*4...*n  Matematical Evaluation
#n! = 1*2*3*3*4...*(n-1)*n
#n! = (n-1)! * n

def factorial_recursive(num): # Factorail using recursion.
    if num == 1 or num == 0: #Base Condition
        return 1
    return num*factorial_recursive(num-1) #FUNCTION calling itself.

print(factorial_recursive(5))

#Working of recursion in this case:

''''Factorial(4) #function called
    4 x Factorial(3)
    4 x [3 x factorial(2)]
    4 x [3 x 2 x factorail(1)]
    4 x 3 x 2 x [1]  #function return '''

#IMPORTANT NOTES:

'''The programer to be careful while working with recursion to ensure that tht function doesn't infinitly keep calling itself. '''
'''Sometimes Recusion is the mst direct way to code an algorithms'''

# PRACTICE_SET CHAPTER_08 :

#QUE_1 Write a program using a function to find greatest of the three numbers.

def maximum(num1,num2,num3): #Function defination.
    if (num1>num2):
        if (num1>num3):
            return num1
        else:
            return num3
    else:
        if (num2>num3):
            return num2
        else:
            return num3

a = maximum(345666,777899,77777) #Function calling.
print("The maximum among them is: " + str(a)) 

#QUE_2 Write a program to convert celsius to farenheit.

def temp(a):
    return a * (9/5) + 32

x= temp(100)
print("The fahrenheit of the given temperature is :" + str(x))

#QUE_3 How do you prevent a python print() function to print a new line at the end.

print("Hello") # Here the value of end is /n thus every print is printed in new line.
print("World")

print("Hello", end= " ") # Now the end value became a space, thus every print will be printed with a space.
print("World")

#QUE_4 Wrie a program to calculate the sum of first n natural numbers.

#Due

#QUE_5 Pattern Printing:

n=3
for i in range(n):
    print("*" * (n-i)) #print "*" (n-1) times.

#Strip Function:
gap = "    Hello World     "
print(gap)
print(gap.strip()) # Removes Extra gap.

#QUE_6 Write a python program to remove an element from a string and strip it at the same time.

def remove_and_strip(string, word):
    newstr = string.replace(word, "")
    return newstr.strip()

gap = "     G Hello World         "
a= remove_and_strip(gap, "G")
print(a)

#QUE_7 Write a python program to print table of any given number.

def table(n):
    for i in range(1,11):
        print(n*i)

a=int(input("Enter the number of which table is required: "))
table(a)

# AUTHOR : RRO-SHAN
# LOCATION : EARTH 286
# DATE : 13TH OF OCTOBER 2021 
# TIME : 6:45 AM IST
