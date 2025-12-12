year=input("Enter the year: ")
if not year.isdigit():
    print("invalid!please enter digits only!")
else:
    year=int(year)
    if year % 400 ==0:
        print(f"{year} is a leap year!")
    elif year % 100==0:
        print(f"{year} is not a leap year!")
    elif year % 4==0:
        print(f"{year} is a leap year!")
    else:
        print(f"{year} is not a leap year!")