#A simple little game using Python
#Using the random library
#v 1.0: added main game functions, basic gameplay
#v 2.0: Will add play again option. Also maybe runtime.

#importing random for random.choice()
def play_rps():

    import random
    # Notifying user with the credits and stuff
    print("Hello, and welcome to RockPaperScissors, credits to @abhishekshahane, v1.0")
    print("You are currently using v1.0. This version will be updated soon to v2.0!")
    print("Use 'git pull' for updating v1.0 to v2.0 as soon as it comes out.")
    # List, input and random.choice(list)
    list = ["Rock","Paper", "Scissors"]
    a=input("Enter a option(First letter in caps):  ")
    b = random.choice(list)
    #Making function errorcheckin
    if (a not in list):
        def errorchecking(a):
            print("Please enter a valid value.")
            print("If you want to play again, run python rps.py")
            exit()
        errorchecking(a)

    # Making main game function
    elif (a in list):
        def rpsmain(a,b):
            b = random.choice(list)
            if b=="Scissors" and a=="Paper":
                print("Computer won, now exiting")
            elif b=="Paper" and a=="Rock":
                print("Computer won, now exiting")
            elif b=="Rock" and a=="Scissors":
                print("Computer won, now exiting")
            elif a=="Scissors" and b=="Paper":
                print("You won, now exiting")
            elif a=="Paper" and b=="Rock":
                print("You won, now exiting")
            elif a=="Rock" and b=="Scissors":
                print("You won, now exiting")
            elif a==b:
                print("Tie")

        rpsmain(a,b)

        playA = input("Do you want to play again (y/n) ?").lower()
        if playA == "y":
            play_rps()
        else:
            exit()

play_rps()
# Calling them at the end of this process
            
