import random
lowest_num=1
highest_num=100
answer=random.randint(lowest_num,highest_num)
guesses=0
is_playing=True
print("Welcome to Number guessing game")
print(f"select a number betweem {lowest_num} and {highest_num}: ")
while is_playing:
    guess=int(input("guess a number(1-100): "))
    if  guess.isdigit():
         guesses+=1
         if guess<lowest_num or guess>highest_num:
              print(" please select a number betweem {lowest_num} and {highest_num}:")
         elif guess<answer:
              print("Too low! The number should be higher than this")
         elif guess>answer:
              print("Too high! The number should be lower than this")
         else:
              print(f"CORRECT!The answer was {answer}")
              print(f"Number of guesses: {guesses}")
              is_playing=False
    else:
         print("invalid")
