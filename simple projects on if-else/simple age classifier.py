age=input("How old are you? ")
if age.isalpha():
    print("invalid!we don't consider alphabets as age!")
else:
    age=int(age)
    if age<13:
        print("you are a child")
    elif age>=13 and age<=19:
        print("you are a teen")
    else:
        print("you are an adult")