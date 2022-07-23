# DICTIONARY : COLLECTION OF KEYVALUE PAIRS.
dict_1 = {                          # e.g of dictionary
    "Fast" : "In a quick manner",
    "Slow" : "In a lazy manner",
    "Marks" : [1,4,5,6,6,6,6,6],
    "dict_within_dict" : { "Player" : "Who plays something", # Example of "NESTED" dictionary
                           "Listener" : "Who listen to something "}
    }
print(dict_1['Fast'])
print(dict_1['Slow'])
print(dict_1["Marks"])
print(dict_1["dict_within_dict"]["Player"])
print(dict_1["dict_within_dict"]["Listener"])

# PROPERTY OF DICTIONARY
''' 1. UNORDERED
    2. MUTABLE
    3. INDEXED '''

# METHODS OF DICTIONARY

dict_1 = {                         
    "Fast" : "In a quick manner",
    "Slow" : "In a lazy manner",
    "Marks" : [1,4,5,6,6,6,6,6],
    "dict_within_dict" : { "Player" : "Who plays something", # Example of "NESTED" dictionary.
                           "Listener" : "Who listen to something "},
    1: 2
    }

print(dict_1.keys()) # throws of keys in a specific dictionary.
print(type(dict_1.keys())) #throws type of dictinary. "(dict_keys)""
print(list(dict_1.keys())) #changes type of dictinory from "dict_keys" to a "list".
print(dict_1.values()) #gives of values in a specific dictionary.
print(dict_1.items()) #gives of key value pairs, in a format of (key,value).

updatedict_1 = {     #updateing dictanary by adding key value pairs.
    "Lovish" : "Friend",
    "Hello"  : "World"
    }
dict_1.update(updatedict_1)
print(dict_1)

# RELEVENCE OF ".get"
print(dict_1.get("Hello")) #returns value if present.
print(dict_1["Hello"]) #returns value if present.

print(dict_1.get("Hello1")) #returns NONE if not present.
# print(dict_1["Hello1"]) #returns AN ERROR if NOT present.


# SETS IN PYTHON : collection of unique( NON-repitative) elements.
a = {1,4,5,6,7,1}
print(type(a))
print(a)

#IMPORTANT : This synatx will create an empty dicionary and not a empty set.
a={}
print(type(a))

#An empty set can be created as follows:
b = set()
print(type(b))

#SETS METHODS:
b= set()
b.add(7) #Adding elements in a set.
b.add(8) 
b.add(8) #Adding a value repeatedly does not changes the set.
b.add((4,5,6,6,7)) #set within a set.
#We cannot add list or dict in a set as they are non hashable.
print(b)

print(len(b)) #return length of a set
#b.remove(6) #as "6" is not present in this given set, as an element it will show an error.
b.remove(7) #remove element "7" from the set.
print(b)

print(b.pop()) #removes an arbitary element form a set.
print(b)

print(b.clear()) #removes all the elmemts of a set.
print(b)

print(b.union({930,373})) #returns the union of set "b" and given set of elemnts. XXXXXXXXXX
print(b)

print(b.intersection({7,8})) #returms the intersection of set "b" and given set of elements. XXXXXXXXXXX
print(b)

# PROPERTY OF DICTIONARY
''' 1. UNORDERED
    2. IMMUTABLE
    3. UNINDEXED 
    4. NO DUPLICATION'''

#CHAPTER_5 PRACTICE SET:

#QUE_1 Write a program to create a dictionary of Hindi words with the value as their english translation.Provide user with an option to look it up!

trans_dict = {
    "khanna" : "Food",
    "Vastu"  : "Object",
    "Dabba"  : "Box"}
print("Options:", trans_dict.keys())
a= input("Enter the Hindi words: ")
#print("Meaning of your word is: ", trans_dict[a])
#BELOW LINE WILL NOT A ERROR IF THE USER ENTER THE KEY WHICH IS NOT IN THE DICTIONARY.
print("Meaning of your word is: ", trans_dict.get(a))

#QUE_2 Write a program to input eight number from the user and display all the numbers(once).

n1=input("enter the first number: ")
n2=input("enter the second number: ")
n3=input("enter the third number: ")
n4=input("enter the forth number: ")
n5=input("enter the fifth number: ")
n6=input("enter the sixth number: ")
n7=input("enter the seventh number: ")
n8=input("enter the eighth number: ")

s = {n1,n2,n3,n4,n5,n6,n7,n8}
print(s)

#QUE_3 Can we have a set with 18(int) & "18"(str) & float(18.1) as a value in it?

p= {18,"18",18.1}
print(p)
# Yes

#QUE_4 What will be the value of the following set:

s= set()
s.add(20)
s.add(20.0)
s.add("20")
print(len(s)) # 2 as value of 20 and 20.0 will be same so pyhton will consider them the same.
print(s)

s= set()
s.add(20)
s.add(20.1)
s.add("20")
print(len(s)) # 3 as there the three unique values.
print(s)

#QUE_5 What is the tyoe of s={}

s = {}
print(type(s))
#ANS. Dictionary

#QUE_6 Create a empty dictionar,allow 4 freinds to enter their fav. language as a values and use keys as their names. Assume that the name are unique.

favlang = {}
a=input("Enter your favorite language person_1: ")
b=input("Enter your favorite language person_2: ")
c=input("Enter your favorite language person_3: ")
d=input("Enter your favorite language person_4: ")

favlang["john"] = a
favlang["sam"] = b
favlang["haris"] = c
favlang["harry"] = d

print(favlang)

#QUE_7 WHAT WILL BE THE OUTPUT WHEN NAMES OF TWO FRIENDS ARE SAME IN QUE_6.

favlang = {}
a=input("Enter your favorite language person_1: ")
b=input("Enter your favorite language person_2: ")
c=input("Enter your favorite language person_3: ")
d=input("Enter your favorite language person_4: ")

favlang["john"] = a
favlang["john"] = b # value of key "john" will be overwrited, and will be printed once.
favlang["haris"] = c
favlang["harry"] = d

print(favlang)

#QUE_8 CAN YOU CHANGE THE VALUE INSIDE A LIST WHICH IS CONTAINED IN SET 5.
#ANS. FIRST OF ALL SET CAN'T CONTAINS A LIST.AND IF WE ASSUME IT IS POSSIABLE, WE WILL NOT BE ABLE TO CHANGE THE VALUE INSIDE A TUPLE AS THEY ARE IMMUTABLE.
#HENCE: NO. MOREOVER IT IS A WRONG QUESTION TO ASK.

# AUTHOR : RRO-SHAN
# LOCATION : EARTH 286
# DATE : 8TH OF OCTOBER 2021 
# TIME : 9:50 PM IST