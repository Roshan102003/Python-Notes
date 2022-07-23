#PROJECT_2: THE PERFECT GUESS

import random
randNumber = random.randint(1,100)

guesses = 0
userGuess = None

while(userGuess != randNumber):
    userGuess = int(input("Enter your guess: "))
    guesses +=1
    
    if(userGuess ==randNumber):
        print("You Guessed it right!")
    else:
        if(userGuess>randNumber):
            print("You guessed it wrong! Enter a smaller number.")
        else:
            print("You guessed it wrong! Enter a Larger number.")

print(f"You guessed the number in {guesses} guesses.")

with open("highscoreproject_2.txt", "r") as f:
    hiscore = int(f.read())

if(guesses<hiscore):
    print("You have just broke the high score!")
    with open("highscoreproject_2.txt", "w") as f:
        f.write(str(guesses))

# AUTHOR : RRO-SHAN
# LOCATION : EARTH 286
# DATE : 31TH OF OCTOBER 2021 
# TIME : 11:25 PM IST



