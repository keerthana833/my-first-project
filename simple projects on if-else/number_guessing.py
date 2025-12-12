actual_number=6
num=input("Guess a number: ")
if num.isalpha():
    print("invalid! please enter digits only!")
else:
    num=int(num)
    if num<0 or num>10:
        print("please select number between (1-10)")
    elif num==actual_number:
        print("CORRECT!")
    elif num<0 and num>10:
        print("please select number between (1-10)")
    elif num<actual_number:
        print("Too low! try again")
    else:
        print("Too high! try again")
