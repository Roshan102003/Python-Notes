#  CREATING A LIST USING []
a = [1,4,6,7,3,9]
print(a) # Printing the list

print(a[0]) # Accessing variour value assigned to a index in a list.
print(a[1])
print(a[2])

a[0] = 10 # Mutating the value in list as list are "MUTABLE".
print(a)

#LIST CAN STORE VALUE OF DIFFERENT DATATYPES.
b = [2,False,"Hello",4.9]
print(b)

#LIST SLICING [same as slicing of string].
students = ["Haris","Tim","Jake","Sunny",23]
print(students[0:4])
print(students[:5])
print(students[3:])
print(students[-4:]) #-4th element will be included.
print(students[:-4]) #-4th element will "NOT" be included.

#LIST METHODS
l1 = [1,3,4,6,7,2,9]

l1.sort() #sorting of list.
print(l1)

l1.reverse() #reverses the sorted list.
print(l1)

l1.append(23) #add new elements to list.
print(l1)

l1.insert(3,8) #add new element at a specific index of a list.
print(l1)

l1.pop(3) #removes an element at a specific index.
print(l1)

l1.remove(9) #removes the given element from list.
print(l1)

l1.clear() # removes all the elemets of list.
print(l1)

#TUPLES 
t = (1,2,4,5)
print(t[0]) #printing zeroth element of a tuple.

#[tuples are immutable]
#t[0] = 54 will show an error.

#DECLARATION OF TUPLES:
t1 = () # Empty tuple
t1 = (1) #Wrong way to declare a tuple with single element.
t2 = (1,) #Tuple with a single element.
print(t2) 

#TUPLES METHODS
t1 = (1,1,1,1,2,3,1,4,5,1)
print(t1.count(1)) # returns number of occurance of value.
print(t1.index(5)) # returns the index of the given element.

# TIME : 7:30 AM IST "PAUSE"

# PRACTICE SET CHAPTER_4

#QUE_1 Write a code to insert 7 elemwnts in a list by asking user.

e1 = input("Enter element number 1: ")
e2 = input("Enter element number 2: ")
e3 = input("Enter element number 3: ")
e4 = input("Enter element number 4: ")
e5 = input("Enter element number 5: ")
e6 = input("Enter element number 6: ")
e7 = input("Enter element number 7: ")
elementlist = [e1,e2,e3,e4,e6,e7]
print(elementlist)

#QUE_2 Write a code to insert marks of 6 students and dispaly them in sorted manner.

s1 = int(input("Enter the marks of student_1: "))
s2 = int(input("Enter the marks of student_2: "))
s3 = int(input("Enter the marks of student_3: "))
s4 = int(input("Enter the marks of student_4: "))
s5 = int(input("Enter the marks of student_5: "))
s6 = int(input("Enter the marks of student_6: "))
studentlist = [s1,s2,s3,s4,s5,s6]
studentlist.sort()
print(studentlist)

#QUE_3 Write a program to sum a list with 4 numbers.

num = [1,6,7,8]
print(sum(num))

#QUE_4 Write a programm to count number of zeros in a list.

list1 = [1,2,4,0,0,0,0,4,5,6,8,8]
print(list1.count(0))

# AUTHOR : RRO-SHAN
# LOCATION : EARTH 286
# DATE : 7TH OF OCTOBER 2021 
# TIME : 1:05 PM IST