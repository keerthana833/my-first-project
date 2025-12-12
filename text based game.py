print("WELCOME TO THE MYSTIC FOREST!")
name=input("What is your name? ")
age=int(input("How old are you? "))
print(f"Hello {name}, you are {age} years old!")
if age>=18:
    print("You are old enough to play!")
    play=input("Do you want to play?(y/n) ").lower()
    health=10
    
    if play=="y":
        print(f" you are going to start with {health} health points")
        print("Let's get into the adventure...")
    else:
        print("have a great day!")
        quit()
           
else:
    print("Sorry! you are not old enough to play!")
    quit()

first=input("path spilt into two...Left or Right?(left/right) ")
if first=="left":
    print("you lead to a river")
else:
    print("sorry you lost the game!GAME OVER")
    quit()

        
river=input("As you lead to river... you want to swim across or build a raft?(across/raft) ")
if river=="across":
    print("you crossed the river but lost 5 health points.")
    health-=5
    
    
else:
    print("You lead to a dark cave...")
    cave=input("want to enter the cave or turn around?(enter/turn around) ").lower()
    if cave=="enter":
        print("You are safe but you fight with bats and lost 3 health with no treasure..")
        health-=3
        print("you lost your 3 health points and the treasure ")
        print(f"you are eliminated with {health} points..Thanks for playing!")
        quit()
    else:
        print("you find a secret tunnel to the temple.")
temple=input("inside the temple,you will face a guardian spirit.You want to fight or offer respect?(fight/respect) ").lower()
if temple=="fight":
    print("you lost your health...GAME OVER!")
    health-=5
    print(f"you got Eliminated with {health} health points....")
    quit()
else:
    print("spirit blesses you and gives treasure peacefully ... so you WON!" )
if health>0:
    print("Congratulations! you found the lost treasure of the mystic forest!")

else:
    print("You collapse before reaching the treasure.GAME OVER!")
    quit()
print(f"You Won the game with {health} health points...You are strong enough DUDE..")
print("Thanks for playing!")

    
    
