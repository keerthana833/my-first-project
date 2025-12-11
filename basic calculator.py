# basic calculator
num1=float(input("enter 1st number: "))
num2=float(input("enter 2nd number: "))
operator=input("enter an operator(+ - * /): ")

if operator=="+":
    result=num1+num2
    print(round(result,2))
elif operator=="-":
    result=num1-num2
    print(round(result,2))
elif operator=="*":
    result=num1*num2
    print(round(result,2))
elif operator=="/":
    result=num1/num2
    print(round(result,2))
else:
    print(f"{operator} is an invalid operator")
print(f"The value: {result}")
