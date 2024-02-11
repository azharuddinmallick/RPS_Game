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
