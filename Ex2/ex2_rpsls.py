#!/usr/bin/env python3
import random
from ex2_rpsls_helper import get_selection

# a function which picks the user and comp selections
def inputs_player_comp():
    #user's choice
    #checks if the player selection is legal (from 1-5)
    tplayer_choice=0
    while (tplayer_choice<1 or tplayer_choice>5):
        tplayer_choice=int(input("    Please enter your selection:"+
                                " 1 (Rock), 2 (Paper), 3 (Scissors), 4"+
                                " (Lizard) or 5 (Spock): "))
        if (tplayer_choice>=1 and tplayer_choice<=5):
            break
        else:
            print("    Please select one of the available options.\n")
            continue
    #comp choice 
    tcc=random.randint(1,5)
    
    return (tcc,tplayer_choice)

# a function which creates a single "mini game" 
def rpsls_game():
    draw_count=0
    player_count=0
    comp_count=0
    winner=0
    
    #the game loop
    while abs(winner)!=2:   

        #call the function we built to get the selections and prints choices
        cc,player_choice=inputs_player_comp()
        print("    Player has selected: %s." %(get_selection(player_choice)))
        comp_choice=get_selection(cc)
        print("    Computer has selected: %s." %comp_choice)
        #############   the game logic  ############
        
        #logic of draw
        if cc==player_choice:
            print("    This round was drawn\n")
            draw_count+=1

        #logic of rock
        #player winning 
        if (player_choice==1 and cc==4):
            print("    The winner for this round is: Player\n")
            player_count+=1
            winner+=1
        if (player_choice==1 and cc==3):
            print("    The winner for this round is: Player\n")
            player_count+=1
            winner+=1
        #player losing
        if (player_choice==1 and cc==2):
            print("    The winner for this round is: Computer\n")
            comp_count+=1
            winner-=1
        if (player_choice==1 and cc==5):
            print("    The winner for this round is: Computer\n")
            comp_count+=1
            winner-=1

        #logic of paper
        #player winning
        if (player_choice==2 and cc==1):
            print("    The winner for this round is: Player\n")
            player_count+=1
            winner+=1
        if (player_choice==2 and cc==5):
            print("    The winner for this round is: Player\n")
            player_count+=1
            winner+=1
        #player losing
        if (player_choice==2 and cc==3):
            print("    The winner for this round is: Computer\n")
            comp_count+=1
            winner-=1
        if (player_choice==2 and cc==4):
            print("    The winner for this round is: Computer\n")
            comp_count+=1
            winner-=1

        #logic of scissors
        #player winning
        if (player_choice==3 and cc==2):
            print("    The winner for this round is: Player\n")
            player_count+=1
            winner+=1
        if (player_choice==3 and cc==4):
            print("    The winner for this round is: Player\n")
            player_count+=1
            winner+=1
        #player losing
        if (player_choice==3 and cc==1):
            print("    The winner for this round is: Computer\n")
            comp_count+=1
            winner-=1
        if (player_choice==3 and cc==5):
            print("    The winner for this round is: Computer\n")
            comp_count+=1
            winner-=1

        #logic of lizard
        #player winning
        if (player_choice==4 and cc==2):
            print("    The winner for this round is: Player\n")
            player_count+=1
            winner+=1
        if (player_choice==4 and cc==5):
            print("    The winner for this round is: Player\n")
            player_count+=1
            winner+=1
        #player losing
        if (player_choice==4 and cc==1):
            print("    The winner for this round is: Computer\n")
            comp_count+=1
            winner-=1
        if (player_choice==4 and cc==3):
            print("    The winner for this round is: Computer\n")
            comp_count+=1
            winner-=1

        #logic of spock
        #player winning
        if (player_choice==5 and cc==1):
            print("    The winner for this round is: Player\n")
            player_count+=1
            winner+=1
        if (player_choice==5 and cc==3):
            print("    The winner for this round is: Player\n")
            player_count+=1
            winner+=1
        #player losing
        if (player_choice==5 and cc==4):
            print("    The winner for this round is: Computer\n")
            comp_count+=1
            winner-=1
        if (player_choice==5 and cc==2):
            print("    The winner for this round is: Computer\n")
            comp_count+=1
            winner-=1

    #prints in the end of this mini game who was the winner and statistics
    if player_count>comp_count:
        print("The winner for this game is: Player")
    else:
        print("The winner for this game is: Computer")     
    print("Game score: Player %d, Computer %d, draws %d"
          %(player_count,comp_count,draw_count))
    
    #defines the last variable which will be what the function returns
    a=winner//2
    return (a)

# A function which creates set of mini-games
# allows with interference to choose amount of sets, quit or continue playing
def rpsls_play():
    set_score=0
    wins_inset=0
    player_decision=0
    player_score=0
    com_score=0
    print("Welcome to the Rock-Scissors-Paper-Lizard-Spock game!")
    while player_decision!=1:
        #decision 3 is to continue with last choice
        if player_decision==3:
            pass
        else:
            N=int(input("Select set length: "))
        #the set game logic
        for i in range(1,N+1): 
            print("Now beginning game %d" %i)
            j=rpsls_game()
            if j==1:
                player_score+=1
            else:
                com_score+=1
            print("Set score: Player %d, Computer %d"
                  %(player_score,com_score))
            if (player_score>(N/2) or com_score>(N/2)):
                break
        #Ha-A-Ra-Cha - what happened if both won same amount
        if player_score==com_score:
            while (abs(player_score-com_score)<2):
                print("Now beginning game %d" %(i+1))
                j=rpsls_game()
                if j==1:
                    player_score+=1
                else:
                    com_score+=1
                print("Set score: Player %d, Computer %d"
                      %(player_score,com_score))
                i+=1
            else:
                pass
        set_score+=1
        #prints the final scores and measeges
        if player_score>com_score:
            print("Congratulations! You have won in %d games."
                  %(player_score+com_score))
            wins_inset+=1
        else:
            print("Too bad! You have lost in %d games."
                  %(com_score+player_score))
        print("You have played %d sets, and won %d!\n"
              %(set_score,wins_inset))
        
        #after finishing the set chosen the ability to chose what to do
        player_decision=int(input("Do you want to: 1 - quit, 2 -"+
              " reset scores or 3 - continue? "))
        if player_decision==2:
            set_score=0
            wins_inset=0
            player_decision=0
            player_score=0
            com_score=0
            print("Resetting scores")
            continue
        if player_decision==3:
            com_score=0
            player_score=0
            i=0

#the debuger helper
if __name__=="__main__": #If we are the main script, and not imported
    from sys import argv
    try:
        random.seed(argv[1]) # as a string is good enough
    except:
        pass

    rpsls_play()
