# Exception Handling in python.
'''When we run a programm and some error happens the programm stops working and stop at that point, 
   to avoid this we use Exception Handling in pyhton which prevent the programm to stop rather address about the exception to the user and try to run the programm again.'''

#Example_1: Exception Handling.

'''while(True):
    print("Press 'q' to quit the game")
    a = input("Enter the number:")
    if a == "q":
        break
    try: #this will try to run the code until and error happen and if error happens it will print the below written statement.
        print("Trying....")
        a = int(a)
        if a>6:
            print("You enterd a number greater than 6.")
        else:
            print("You have entered a number which is less than 6.")

    except Exception as e: # THIS AVOID CRASHING OF PROGRAMM AND HANDLES THE ERROR BY PRINTING THE ERROR AND AGIN RUNNING THE PROGRAMM.
        print(f"YOUR INPUT RESULTED IN AN ERROR: {e}")

print("Thanks for playing the game.") '''

#Example_2: Handling Various Exception

'''try:
    a= int(input("Enter a number: "))
    c= 1/a
    print(c)
except ValueError as e: 
    print(f"Please enter a valid value.")

except ZeroDivisionError as e: 
    print(f"Make sure you are not dividing by 0.")

except:
    print("A special type of exception has occured.")

print("Thanks for using the Programm!") '''

#Raising Execeptions:
'''def  increment(num):
    try:
        return int(num) + 1
    except:
        raise ValueError("This is a custom made exception.")

a = increment(34) # will work fine.
print(a)

b= increment("ghhj") # will raise the custom made Exception.
print(b)'''

# try with else clause: else clause in this case is used to insure wether the code ran succesfully or not.
#e.g
'''
try:
     i =int(input("Enter a number: "))
     c = 1/i
     print(c)
except Exception as e:
    print(f"The follwing exception occured:{e}")
else:
    print("The code ran sucessful.") # will be printed when code run without going to the exception part of the programm.

# try with finally :

try:
     i =int(input("Enter a number: "))
     c = 1/i
     print(c)
except Exception as e:
    print(f"The follwing exception occured:{e}")
    #exit()
finally:
    print("Finally the programm is closed.") #this is use to do fininshing the code which will excecute irrespective of exception, even exiting the programm.

#if__name__=="__main__" in python:

def greet(name):
    print(f"Good Morning, {name}")

if __name__ == "__main__": #if we want ot use the above function in another file but don't want the argument to pass through the below written code we use this.
    n=input("Enter a name: ")
    greet(n)

# The Global Keyword : used to modify the variable outside of the current scope.
#e.g

a = 100 #Global Variable
def func_1():
    global a #keyword used to change global value of "a".
    print(f"Print statement 1: {a}")
    a = 500 #Local Variable if global keyword is not used.
    print(f"Print statement 2: {a}")

func_1()
print(f"Print Statement 3:{a}")

#Enumerate function in python: add counter to an iterable and return it,
#e.g

list1 = [3.0,3,55,"Hello",False]
for index, item in enumerate(list1):
    print(item,"Index number: ",index)

#List Comprehensions: An elegant way to create lists based on existing lists.
#e.g

#Simple Way
a = [5,7,8,99,9,33,2,56,100]
b = []
for item in a:
    if item%2 == 0:
        b.append(item)
print(b)

#Elegant Way
b= [i for i in a if i%2==0]
print(b) '''


#PRACTICE SET CHAPTER_12
#QUE_1:Write a program to open thre files 1.txt, 2.txt and 3.txt. If any of these files are not present. a message without exiting the program must be printed prompting the same.

def readFile(filename):
    try:
        with open(filename, "r") as f:
            print(f.read())
    except FileNotFoundError:
        print(f"File {filename} is not Found.")

readFile("1.txt")
readFile("2.txt")
readFile("3.txt")


#QUE_2 : Write a program to print third, fifth, and seventh element from a list using enumerate functions.

list = ["hello","world","hey",10,100,False,200,"Okay",True]
for index, item in enumerate(list):
    if index ==2 or index ==4 or index ==6:
        print(item,"Index number: ",index,"Element No:",index+1)

#QUE_3 Write a list comprehension to print a list which contains the multiplication table of a user entered number.

num = int(input("Enter a number: "))
table = [num*i for i in range(1,11)]
print(table)

#QUE_4 Write a programm to display a/b. If b=0 handle the error.

a = int(input("Enter a the first number: "))
b = int(input("Enter the second number: "))

try:
    print("Result:",a/b)
except ZeroDivisionError:
    print("Infinite.")

#QUE_5 Store the multiplication table generated in question 3 in a file.

num = int(input("Enter a number: "))
table = [num*i for i in range(1,11)]
print(table)
with open("table.txt", "a") as f:
    f.write(str(table))
    f.write("\n")

# AUTHOR : RRO-SHAN
# LOCATION : EARTH 286
# DATE : 22ND OF NOVEMBER 2021 
# TIME : 11:40 AM IST