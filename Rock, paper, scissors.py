import random
i=random.randint(0,2)
a=input("Pick Rock, Paper, or Sisscors...")
if i==0:
    i=("Rock")
    if a==i:
        print("It's a Tie!")
    elif a==("Paper"):
        print("You win Paper covers Rock!")
    elif a==("Sisscors"):
        print("I win, My Rock smashes your Sisscors")
if i==1:
    i=('Paper')
    if a==i:
        print("It's a Tie!")
    elif a==("Sisscors"):
        print("You win your Sisscors cuts my Paper!")
    elif a==("Rock"):
        print("I win, My Paper covers your Rock!")
if i==2:
    i=("Sisscors")
    if a==i:
        print("It's a Tie!")
    elif a==("Rock"):
        print("You win your Rock smashes my Sisscors!")
    elif a==("Paper"):
        print("I win, My Sisscors cuts your Paper!")
if a==("Joey's Cockeroach"):
    print("There is no beating that!!!")
