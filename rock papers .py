
import random
def rocksissors():
    userscore=0
    comscore=0
    play=5
    values=["rock","paper","sissors"]
    result=random.choice(values)
    user=None
    while user not in values:
        for i in range(1,play+1):
            print(f"your {i} round")
            user=input('enter the choice ("rock","paper","sissors") \n')
            if user not in ["rock","paper","sissors"]:
                print('invalid input you lost 1 chance .enter input ("rock","paper","sissors")')
                continue

            print("user input=",user)
            print("computer input=",result)
            if user==values:
                print("tie")
            elif user=="rock" :
                if values=="paper":
                    print("compwin")
                    comscore+=1
                else:
                    print("user win")
                    userscore+=1
            elif user=="paper":
                if values=="rock":
                    print("user wins")
                    userscore+=1
                else:
                    print("computer wins")
                    comscore+=1
            elif user=="siccor":
                if values=="rock":
                    print("computer wins")
                    comscore+=1
                else:
                    print("userr wins")
                    userscore+=1
    print("computer score =",comscore)
    print("userscore=",userscore)
    if comscore<userscore:
        print("user win the game")
    elif comscore==userscore:
        print("Tie match")
    else:
        print("computer win the game")
rocksissors()