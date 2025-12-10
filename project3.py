print("welcome to my first game!")
name=input("what is your name? ")
age=int(input("How old are you? "))


print(f"Hello {name}! you are {age} years old.")
if age>=18:
    print("you are old enough to play!")
    health=10

    game=input("Do you want to play? (y/n)").lower()
    if game=="y":
        print("you are starting with {health} health points.")
        print("Let's begin your adventure...")
    
    
else:
    print("Sorry! you are not old enough to play")
    exit()
        
first=input("you are at a cross road...Left or Right (left/right)? ").lower()
if first=="left":
    print("Nice!You follow the path and reach a lake.")
    second=input("do you swim across or go around? (swim/around): ").lower()
    if second=="swim":
        print(" You tried to swim but lost 5 health")
        health-=5
    else:
        print("You went around safely.")

          
else: 
    print("You fell into a hole. GAME OVER!")
    health-=10
if health<=0:
    print("You have no health left.GAME OVER!")
else:
    print(f"You survived the adventure with {health} health points!")
    
    

    



