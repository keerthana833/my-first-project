correct_username="spongebob"
correct_password="12345"
username=input("Enter your username: ")
password=int(input("Enter your password: "))
if username==correct_username and password==correct_password:
    print("You have logged in successfully!")
else:
    print("Invalid username and password!")