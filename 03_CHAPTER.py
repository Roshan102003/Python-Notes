# DIFFERENT WAYS TO DEFINE A STRING DATATYPE IN PYTHON
a = ' HELLO WORLD"S '
b = " HELLO'S "
c = ''' HELLO"S AND WORLD'S '''
print(a,b,c)

# CONCATINATION OF TWO STRING
wish = "what's up, "
name = "world"
print(type(name))  #CHECKING THE DATATYPE
print(wish + name) 

# SLICING OF TWO STRING
name = "HelloWorld"
print(name[1]) #print the character assigned to a index in a string
print(name[0:3]) #character from index 0 to 3 will be print from the string (excluding 3)
print(name[-1]) #print the last character of string wich is assigned in index "-1"
print(name[-4:-1])
print(name[:5]) #same as [0:5]
print(name[5:]) #same as [5:10]

#SLICING WITH SKIPPED VALUE
x = name[0:9:2] #print all the values assigned from 0 TO 9 with a skip of 1 INDEX. 
y = name[0::3] #print all the values assigned from 0 to LEN of string with a skip of 2 INDEX.
print(x)
print(y)

#ADVANCED SLICING TECHNIQUES examples:-
'''hello[:2]-------->hello[0:2]
   hello[3:]-------->hello[3:5]'''

# STRING FUNCTIONS
story = "this is a sample text story to understand the basics operations on string"
print(len(story))
print(story.endswith("sample")) # gives weather string ends with the given string or not.
print(story.endswith("string"))
print(story.count("t")) # count number of given characters in the string.
print(story.capitalize()) # capitalizes the first character of the first word of the string.
print(story.find("sample")) #tells in which index the following string is located. [ONLY "FIRST" OCCURANCE].
print(story.find("hello")) #will give "-1" if word is not present in the string.
print(story.replace("sample", "demo")) #replaces "ALL" the initial string with final string in a string.

# ESCAPE SEQUENCES CHARACTER
p = "This a first line. \n Second line using the newline escape sequence character. \t sample of tab \'single quotes\' \\backslash"
print(p)

#CHAPTER_3 PRACTICE SET

#QUE_1 Write a code to wish good luck to the user using user name as input.

name = str(input("Enter your name:"))
wish = "good luck "
print(wish + name)

# TIME : 7:30 AM IST "PAUSE"

#QUE_2 Write a program to fill ina letter template given below with name and date.

a=str(input("Enter the name of selected candidate:"))
b=str(input("Enter the date of selection:"))
print("Dear",a,"you are selected !",b)

# OR 

# BY USING REPLACE FUNCTION
a = '''Dear <NAME> you are selected! <DATE>'''
name=input("Enter your name")
date=input("Enter the date")
a = a.replace("<NAME>", name)
a = a.replace("<Date>", date)
print(a)

#QUE_3 Write a program to count number of double spaces in a string.Replace them if present.

q= "This a sample string to detect  double spaces in this string"
v = q.find("  ")
print(v)

q=q.replace("  ", " ")
print(q)

#QUE_4 PRINT THE UNSEQUENCED LETTER IN FORMAT
# letter = "Hello there! Its jack from earth 616......[SIGNAL LOSS]! WE NEED ASSISTANCE....!"

modified_letter = "Hello there! \n Its jack from earth 616.......[SIGNAL LOSS]! \n WE NEED ASSISTANCE....!"
print(modified_letter)

# AUTHOR : RRO-SHAN
# LOCATION : EARTH 286
# DATE : 6TH OF OCTOBER 2021 
# TIME : 9:50 PM IST