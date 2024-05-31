import random
import math

lower=1
upper=100
random_no=random.randint(1,100)

guess=0
max_guess=0

Player_name=input("Enter your name: ")
welcome=input(f"WELCOME  {Player_name} in a Number Guessing Game.")
print("Please Guess a Number between 1 to 100")

print("Start your Game")
while (guess!=random_no):
        guess=int(input("Guess any Random number: "))
        max_guess +=1
        if(guess== random_no):
           print(f"Congratulate!{Player_name} YOU WIN")
           print(f"you have max guess no is : {max_guess}")

        elif(guess>random_no):
             print("Guess Lower")
        elif(guess<random_no):
             print("Guess higher")
           


 



   
  



