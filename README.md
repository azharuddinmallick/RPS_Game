# RPS_Game
import random
user=0
computer=0
ch="y"
while ch=="y" :
    #Input from the user is taken
    print("R for rock")
    print("P for paper")
    print("S for scissors")
    print()
    p1=str(input("Enter your choice :: "))
    if p1=='R' or p1=='r' :
        p1="Rock"
    elif p1=='P' or p1=='p' :
        p1="Paper"
    elif p1=='S' or p1=='s' :
        p1="Scissors"
    #Random choice from the computer is taken 
    seq=["Rock","Paper","Scissors"]
    p2=random.choice(seq)
    print("Computers choice is",p2)
        
    if p1=="Rock" :
        if p2=="Rock" :
            print("Tie")
        elif p2=="Paper" :
            print("You Lose! Paper covers Rock")
            computer+=1
        elif p2=="Scissors" :
            print("You Win! Rock smashes Scissors")
            user+=1
    #Condition if the user choses paper
    elif p1=="Paper" :
        if p2=="Rock" :
            print("You Win! Paper covers Rock")
            user+=1
        elif p2=="Paper" :
            print("Tie")
        elif p2=="Scissors" :
            print("You Lose! Scissors cut Paper")
            computer+=1
    #Condition if the user choses scissors
    elif p1=="Scissors" :
        if p2=="Rock" :
            print("You Lost! Rock smashes Scissors")
            computer+=1
        elif p2=="Paper" :
            print("You Win! Scissors cut Paper")
            user+=1
        elif p2=="Scissors" :
            print("Tie")
    print()
    #The user is asked if he wants to play the game again or not
    ch=str(input("Do you still want to continue? (y/n)"))
    print()
#The score of both the user and the computer is diaplayed seperately
print("User ::",user)
print("CPU ::",computer)
