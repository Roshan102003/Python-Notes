#FILE I/O

#RAM: Random Access memory is volatile and all its contents are lost once the program is terminated.
# In order to persist the data forever we use files which is basically stored in ROM.

#Types of files:
'''1. Text files (.txt etc)
   2. Binary files (.jpg etc)'''

#NOTE:Python has many functions for reading, updating and deleting files.

# Opening a file using pyhton:

#Use open function to read the content of the file.
f = open('sample.txt', 'r')  #opening file in read mode.
a = f.read()                 #reading file.
print(a)                     #printing the content in the file.
f.close()                    #closing file.

#NOTE:If we don't specifiy the mode of open of opening file, the file will open in read mode by default.
#e.g:
f = open('sample.txt')  
a = f.read()                 
print(a)                     
f.close()

#printing specific characters form the file:
f = open('sample.txt')  
a = f.read(4)     #Reads first "4" character of the file.             
print(a)                     
f.close()

# Using Readline function to read file content.
f = open('readline.txt')  
a = f.readline()       #Read the first line of the file.          
print(a)
a = f.readline()       #Read the second line of the file.         
print(a)                  
f.close()

# NOTE:Readlines are used to return all the line present in the file at a single go.

# Modes to open files using python:
'''r: Read Mode
   w: Write Mode
   a: Append Mode
   +: Update Mode = Read and Write Mode'''

# For binary files we use: "rb" mode.
# For text file we use : "rt" mode. Or we can only use "r".

# Writing content in files using "w" :
f = open('write&append.txt', "w")  #opening file in write mode.
f.write("Write this content to the file.")  #Delete the intial content of the file and add the given new content.            
f.close()

# If a file is not present, File is created and content is added by pyhton.

# Writing content in files using "a":
f = open('write&append.txt', "a")  #opening file in append mode.
f.write(" Write this content to the file without deleting the intial content in the file.") #add the given new content to a file without deleting the intial content in the file.            
f.write(" Write this content to the file without deleting the intial content in the file.") #will be appended again.
f.close()

# With Function: By using "with", file will be closed automatically. We didn't need to use close() statement every time.
#e.g:
with open("sample.txt") as f:
    f.read() #Here we didn't have to use close() statement to close the file it will be closed automatically.

#CHAPTER_09 PRACTICE SET:
#QUE_1 Write a program to read the text from a given file "poem.txt" and find out wheather it contains the word "Twinkle".

p = open("poem.txt")
f = p.read()
if "Twinkle" in f:                                #Appling condition.
   print("Twinkle is present in the given file.")
else:
   print("Twinkle is not present in the given file.")
p.close()

'''QUE_2 The game() function in a program lets a user paly a game and return the score as an integer. You need to read a file "History.txt" which is either blank or contains the previous high score.
         Whenever game() breaks the Hi-Score.'''

def game():                       #Defining a function.
   return 66 

score = game()                    #Assining the score to a variable.
with open("high_score.txt") as f: #Reading file
   highscore = (f.read())

if highscore == "":                #When file is blank.
   with open("high_score.txt", "w") as f: #Score will be writted.
      f.write(str(score))  

elif int(highscore)<score:                #Comparing the two scores.
   with open("high_score.txt", "w") as f:
      f.write(str(score))          #Updateing the score in txt file.

'''QUE_3 Write a program to generate multiplication tables from 2 to 20 and write ot to differnet files.Place these files in a folder for a 13-year old.'''

#QUE_4 A File contains a word "Donkey" multiple times. You need to write a program to replace this word with #### by updating the same file.

with open("slang.txt") as f:
   content = f.read()

content = content.replace("donkey", "####")

with open("slang.txt", "w") as f:
   f.write(content)

#QUE_5 Repat program 4 for the list of such words to be cencored.

words = ["donkey","nuckelhead","jerk"]

with open("slang.txt") as f:
   content = f.read()
for word in words:
   content = content.replace(word, "####")

with open("slang.txt", "w") as f:
   f.write(content)

#QUE_6 Write a program t o find a log file and find out wheather it contains "python".

with open("log.txt") as f:
   content= f.read().lower() #convert the file content in lower case.

if "python" in content:
   print("Yes, python is present in the log.")
else:
   print("No, pyhton is not present.")

#NOTE: lower is use to convert the file content to lower case, to ALSO identity "Pyhton" key word FROM THE CONTENT in this case.\

#QUE_7 Write a program to find out the line number where the keyword "pyhton" is present.

content = True
i = 1 #counter

with open("log.txt") as f:
   while content:
      content= f.readline()
      
      if "python" in content.lower():
         print(content)
         print(f"Yes, python is present on line number: {i}")
      i+=1

#QUE_8 Write a program to make a copy of a text file "this.txt".

with open("this.txt") as f:
   content = f.read()
with open("copy.txt", "w") as f: 
   f.write(content)     #content of the file "this" will be copied to copy.txt file.

#QUE_9 Writea aprogram to check the two file's content were identical or not:

file_1 = "copy.txt"
file_2 = "this.txt"

with open(file_1) as f:
   file_1 = f.read()

with open(file_2) as f:
   file_2 = f.read()

if file_1 == file_2:
   print("Files are identical.")
else:
   print("Files are not identical.")

#QUE_10 Write a program to wipe out all the content of the file using python.

with open("wipe.txt", "w") as f:
   f.write("") #overwrite the file to nothing as input is blank.

#QUE_11 Write a progeram to rename to "wiped_content_renamed.txt".

import os   #importing os module
oldname = "wipe.txt"
newname = "wiped_content_renamed.txt"

with open(oldname) as f:
   content = f.read()

with open(newname, "w") as f:  #appending the content of old file in new file.
   f.write(content)

os.remove(oldname) #removing the old file i.e wipe.txt

# AUTHOR : RRO-SHAN
# LOCATION : EARTH 286
# DATE : 26TH OF OCTOBER 2021 
# TIME : 8:55 AM IST