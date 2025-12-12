temp=input("What is the temperature in celcius? ")
if temp.isalpha():
    print("invalid!")
else:
    temp=int(temp)
    if temp<=0:
        print("it's freezing")
    elif temp<=20:
        print("it's cold")
    elif temp<=35:
        print("it's warm")
    elif temp>35:
        print("it's hot")
    else:
        print("invalid temperature")