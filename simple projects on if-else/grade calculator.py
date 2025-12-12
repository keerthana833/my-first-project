marks=input("Enter your marks (0-100): ")
if marks.isalpha():
    print("invalid! please enter digits!")
else:
    marks=int(marks)
    if  marks<0 or marks>100:
        print("invalid! please enter marks between (0-100)")
    elif marks>=90:
        print("grade A")

    elif marks>=75:
        print("grade B")   

    elif marks>=50:
        print("grade C")
    else:
        print("you failed the exam")   


