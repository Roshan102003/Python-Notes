# Conditional Expressions : Output depending upon some conditons.

# if and elif: are a mulitway desicion taken by the program due to certain condition in our code.

from typing import Text, TextIO


a= 45   #eg. of if-elif-else ladder.
if(a>3):
    print("the value of a is grater than 3") #python will first check this condition. If satisfied output will be printed and the interpretor will not go to the second conditional.
elif(a>7):
    print("the valure of a is grater than 7") #if first one didn't fullfill the condition, python will check the next conditional. If satisfied, output will be printed. If not it again move to the next one.
elif(a>8):
    print("the valure of a is grater than 8")  #WE CAN MULTIPLE CONDITONALS IN A CASE BY USING "ELIF" CONDITIONALS.
elif(a>9):
    print("the valure of a is grater than 9")
elif(a>19):
    print("the valure of a is grater than 19")
else:                                            
    print("the value is not grater than 3 or 7") #if none of the conditonal will satisfy, pyhton will print this.

#QUICK_QUIZ : Write a program to print yes when the age entered by the user is grater than or equal to 18.

age=int(input("Please enter the age of person: "))
if(age>=18): #HERE WE HAVE USED RELATIONAL OPERATION.
    print("Yes, the person is eligiable to vote.")
else:
    print("Sorry, you are not eligaible to vote.")

# RELATIONAL OPERATORS : used to evaluate the condition inside the "if" statement, eg: ==,>=,<=,etc.
#eg.
age=int(input("Please enter the age of person: "))
if(age>=18): #HERE WE HAVE USED RELATIONAL OPERATION.
    print("Yes, the person is eligiable to vote.")
else:
    print("Sorry, you are not eligaible to vote.")

# LOGICAL OPERATORS : used to operate conditional statement. eg. AND,OR,NOT.
#eg.
job= int(input("Enter the age of the candidate."))
if(job>45 and job<60): #HERE WE HAVE USED LOGICAL OPERATION.
    print("You are selected")
else:
    print("Sorry you are not eligiable.")

#"IN" AND "IS" CONDITONALS:

#eg. of "IS"  
a = 45
if (a is 45): #Checks the value of a variable.
    print("YES")
else:
    print("NO")

#eg. of "IN"  
z= [3,6,56]
print(456 in z) #Check wheather the given value exist in the given list or not.

# IMPORTANT NOTES:
'''1.There can be any number of elif statements in a ladder.
   2.Last else will only be executed if all the conditons inside elifs fails.'''
 
#CHAPTER_6 PRACTICE SET.
#QUE_1 Write a program to find the greatest among the 4 numbers enter by user.

n1=int(input("Enter the 1st number: ")) 
n2=int(input("Enter the 2nd number: "))
n3=int(input("Enter the 3rd number: "))
n4=int(input("Enter the 4th number: "))

if(n1>n4): #n1 vs n4
    f1 = n1
else:
    f1 = n4

if(n2>n3): #n2 vs n3
    f2 = n2
else:
    f2 = n3 

if(f1>f2): # winner f1 vs f2
    print(str(f1) + " is greatest")
else:
    print(str(f2) + " is greatest")
    
#QUE_2  Wrie a program to find out wheather a student is pass or fail, if it requires total 40% and at least 33% in each subject to pass
#Assume 3 subject and take marks from the user.

s1=int(input("Enter your subject_1 marks: "))
s2=int(input("Enter your subject_2 marks: "))
s3=int(input("Enter your subject_3 marks: "))

if(s1<33 or s2<33 or s3<33):
    print("You are Fail")
elif(s1+s2+s3)/3 <40:
    print("You are Fail")
else:
    print("You are Pass")

#QUE_3 Spam Detector.

comment= input("Enter the text: ")

if("make a lot of money" in comment):
    print("The comment contains a spam.")
elif("click this" in comment):
    print("The comment contains a spam.")
elif("buy now" in comment):
    print("The comment contains a spam.")
elif("subscribe this" in comment):
    print("The comment contains a spam.")
else:
    print("The comment doesn't contain any spam. ")

#QUE_4 Write a program to find out wheather a given username conatins less than 10 characters or not.

username=str(input("Enter your username: "))
a=len(username)

if (a<10):
    print("The username comtains less than 10 characters.")
else:
    print("The username contains more than or equal to 10 characters.")

#QUE_5 Write a program which finds out wheather a given list contain the given name in it or not.

name = ["tesla","intel","microsoft","adobe","google"]
user_name=input("Enter the name: ")

if(user_name in name):
    print("Th name is in the list.")
else:
    print("The name is not in the list.")

#QUE_6 Write program to calculate the grade of a student from his marks.

marks=int(input("Enter you marks: "))

if (90<marks<=100):
    print("EXCELLENT")
if (80<marks<=90):
    print("A")
if (70<marks<=80):
    print("B")
if (60<marks<=70):
    print("C")
if (50<marks<=60):
    print("D")
if (40<marks<=50):
    print("E")
else:
    print("F")

#QUE_7 Write a program to find the given post talks about ALIENS or not.

post=str(input("Enter the post here: "))

if("ALIENS" in post):
    print("The post is talking about Aliens.")
else:
    print("The post is not talking about Aliens.")

# AUTHOR : RRO-SHAN
# LOCATION : EARTH 286
# DATE : 10TH OF OCTOBER 2021 
# TIME : 2:10 PM IST