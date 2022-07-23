#SNAKE,WATER AND GUN.
import random

def game_win(comp,you):
    if comp == you:
        return None
    
    elif comp == "s": 
        if you=="w":
            return False
        elif you == "g":
            return True

    elif comp == "w":
        if you=="s":
            return True
        elif you == "g":
            return False

    elif comp == "g":
        if you=="s":
            return False
        elif you == "w":
            return True
    
print("Comp Turn: Snake(s) Water(w) or Gun(g) ? ")
rand_number= random.randint(1,3)

if rand_number == 1:
    comp = "s"
elif rand_number == 2:
    comp = "w"
elif rand_number == 3:
    comp = "g"

you = input("Your Turn: Snake(s) Water(w) or Gun(g): ")
a = game_win(comp,you)

print(f"Computer choose {comp}")
print(f"You choose {comp}")

if a == None:
    print("The game is tie!")
elif a:
    print("You Win!")
else:
    print("You Lose!")

# AUTHOR : RRO-SHAN
# LOCATION : EARTH 286
# DATE : 13TH OF OCTOBER 2021 
# TIME : 7:15 AM IST