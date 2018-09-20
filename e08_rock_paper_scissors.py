again = True
while(again):
    a_play = input("Player One: ")
    b_play = input("Player Two: ")
    if(a_play == "Rock"):
        if(b_play=="Scissors"):
            print("Player One wins")
        elif(b_play=="Paper"):
            print("Player Two wins")
        else: print("Tie")
    elif(a_play == "Paper"):
        if(b_play=="Scissors"):
            print("Player Two wins")
        elif(b_play=="Paper"):
            print("Player One wins")
        else: print("Tie")
    else:
        if(b_play=="Scissors"):
            print("Tie")
        elif(b_play=="Paper"):
            print("Player One wins")
        else: print("Player Two Wins")
    if input("Play again?")=="n": again = False