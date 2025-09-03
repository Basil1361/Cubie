
import random

def RockPaperScissors(): 
    list_name = list("rps")
    while True:
        c = random.choice(list_name)
        x = input("Choose r, p, s: ").lower()
        if x not in ("r", "p", "s"):
            print("Retype!")
            continue
        if x == "q":
            print("Goodbye!")
            break
        print("Player Hand:",x,"Computer Hand:", c)
        if x == c:
            print("Tie")
        elif (x == "r" and c == "s") or \
            (x == "p" and c == "r") or \
            (x == "s" and c == "p"):
            print("Player Wins")
        else:
            print("Computer Wins")
            
RockPaperScissors()