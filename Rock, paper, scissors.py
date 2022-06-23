import random
comchoice=random.randint(0,2)
userpick=input("Pick Rock, Paper, or Sisscors...")
if comchoice==0:
    comchoice=("Rock")
    if userpick==comchoice:
        print("It's a Tie!")
    elif userpick==("Paper"):
        print("You win Paper covers Rock!")
    elif userpick==("Sisscors"):
        print("I win, My Rock smashes your Sisscors")
if comchoice==1:
    comchoice=('Paper')
    if userpick==comchoice:
        print("It's a Tie!")
    elif userpick==("Sisscors"):
        print("You win your Sisscors cuts my Paper!")
    elif userpick==("Rock"):
        print("I win, My Paper covers your Rock!")
if comchoice==2:
    comchoice=("Sisscors")
    if userpick==comchoice:
        print("It's a Tie!")
    elif userpick==("Rock"):
        print("You win your Rock smashes my Sisscors!")
    elif userpick==("Paper"):
        print("I win, My Sisscors cuts your Paper!")
if userpick==("Joey's Cockeroach"):
    print("There is no beating that!!!")


