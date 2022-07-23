# LOOPS IN PYHTON :  Make our work easy by repeating intructions.

#There are two types of loop in pyhton.
'''1.While
   2.For'''

#eg. of while loop
i=1
while i<=10:
    print("Roll_no: " + str(i))
    i=i+1
print("Attendence Done")

#QUICK_QUIZ: Wriie a program to print 1 to 50 using a while loop.
a=1
while a<51:
    print(a)
    a=a+1
print("Program has been successfully executed")

#QUICK_QUIZ: Write a program to print A string 5 times.
i= 0
while i<5:
    print("Trouble times")
    i=i+1

#INFINITE LOOP: Loop in which the condition never become false.
#eg. 
'''a=0
while a<10:
    print("INFINITE LOOP EXECUTION")'''

#NOTE: If the condition never become false, the loop keep geeting executed.And it is called Infinite loop.
 
#QUICK_QUIZ: Write a program to print content of a list using while loop.
Fruits = ["Apple","Banana","Orange","Watermelon"]
i = 0
while i<len(Fruits):
    print(Fruits[i])
    i=i+1
print("ALL the Fruits list has been executed.")

# For loop: Used to iterate through a sequence like list,tiuple or string [iterables].

#eg.
Fruits = ["Apple","Banana","Orange","Watermelon"]
for i in Fruits:
    print(i)
print("ALL the Fruits list has been executed.")

# "Range" in python : used to generate a sequence of number.

#eg.
for i in range(8): #print number from 0 to 7
    print(i)
#eg.
for i in range(1,8): #print number from 1 to 7.
    print(i) 
#eg.
for i in range(1,8,2): #print number from 1 to 7 with a step_size(gap) of 2.
    print(i)

# For loop with else:
for i in range(11):
    print(i)
else:
    print("The program has been executed.") #executed when for loop get exhausted.

# Break statements:

for i in range(10):
    print(i)
    if i == 5: #over_command the condition and breaks the loop there immediatly.
        break
else:
    print("The loop has been completed.") #this will execute only when the loop execute completely.

# Continue statements:

for i in range(10):
    if i == 5: # skips the given value and print other value normally.
        continue
    print(i)

# pass statement :NULL statement in python.

i = 4
if i>0:
    pass # used to do nothing do get rid of errors.
print("The programm has been pass for a while.")

#PRACTICE SET CHAPTER_07

#QUE_1 Write a program to print multiplication table of a given number using for loop.

num=int(input("Enter the number of which the table is required: "))

for i in range(1,11):
    print(str(i*num))

#QUE_2 Write a program to great all the person names stored in a list l1 and which starts with "S".

l1=["Sohan","Sam","Suman","Martin","Tesla"]

for name in l1:
    if name.startswith("S"):
        print("Hello " + name)
    else:
        print("There is no name starting from 'S' ")

#QUE_3 Write a program to find wheather the given nmuber is prime or not.

num=int(input('Enter the number here: '))

for i in range(2,num):
    if(num%i == 0):
        print("The number is not prime.")
        break
    else:
        print("This number is prime.")
        break

#QUE_4 Write a program to find the sum of first n natural numbers using while loop.

a= int(input("Enter the number upto which sum is required: "))
i=1
while i<=a:
    print(i)
    i=i+1
print("Program executed.") #"CON"

#QUE_5 Wrie a program to calculate factorial of anumber using for loop.

fac=int(input("Enter the number of which the factorial is required: "))
factorial = 1

for i in range(1,fac+1):
    factorial = factorial * i
print(f"The factorial of the {fac} number is {factorial}")
    
#QUE_6 Write a program to print the star as follows:

''' *
    ***
    *****  ''' 

n =int(input("Enter the number of rows reqired: "))

for i in range(n):
    print("*" * (i))

#QUE_7 Write a program to print the star as follows:

'''   *
     ***
    *****  ''' 

n=int(input("Enter the number of rows required: "))

for i in range(n):
    print(" " * (n-1-i), end = "")
    print("*" * (2*i+1), end = "")
    print(" " * (n-i-1))

#QUE_7 Write a program to print the star as follows:

'''  ***
     * *
     *** ''' 
#ANS:

#QUE_8 Write a program to print multiplication tab;e of "n" using for loop in reverse ordere.
#ANS :
num = int(input("Enter the number of which reverse table is required: "))
for i in range(1,11):
    print(i)

# AUTHOR : RRO-SHAN
# LOCATION : EARTH 286
# DATE : 11TH OF OCTOBER 2021 
# TIME : 5:13 PM IST