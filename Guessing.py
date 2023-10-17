import random
import math
a=int(input("Enter the Range Strating Point: "))
b=int(input("Enter the Range Ending Point: "))
c=random.randint(a,b)
print("\n\tYou Have Only ",round(math.log(b-a+1,2))," Chances to guess the integer!\n")
# print(c)
count=0
print("Let's Start the Game")
while count<math.log(b-a+1,2):
    count+=1
    d=int(input("Enter Your Guess: "))
    if(d>c):
        print("Try Again! You Guessed Too High")
    elif(c>d):
        print("Try Again! You Guessed Too Small")
    else:
        print("You Guessed It Right")
        break
if count>=math.log(b-a+1,2):
    print("\nThe no. is %d"%c)
    print("\tBetter luck next time!")

