
# # A Card Game
import random
string=["A",2,3,4,5,6,7,8,9,10,"J","Q","K"]
b=random.choice(string)

print("Let's Play A Card Game")
a=input("Enter your card value: ")
# b=input("Enter your card value: ")
print("Computer's card Value: ",b)
    
if(a<b):
        print("YOU LOSS")
    
elif((a=="A" or b=="J") or (a=="A" or b=="Q") or (a=="A" or b=="K") or (a=="A" or b==2) 
       or (a=="A" or b==3) or (a=="A" or b==4) or (a=="A" or b==5) or (a=="A" or b==6) 
       or (a=="A" or b==7) or (a=="A" or b==8) or (a=="A" or b==9) or (a=="A" or b==10)
       or (a=="J" or b==3) or (a=="J" or b==4) or (a=="J" or b==5) or (a=="J" or b==6) 
       or (a=="J" or b==7) or (a=="J" or b==8) or (a=="J" or b==9) or (a=="J" or b==10)
       or (a=="J" or b==2)
       or (a=="Q" or b==3) or (a=="Q" or b==4) or (a=="Q" or b==5) or (a=="Q" or b==6) 
       or (a=="Q" or b==7) or (a=="Q" or b==8) or (a=="Q" or b==9) or (a=="Q" or b==10)
       or (a=="Q" or b==2) or (a=="Q" or b=="J")
       or (a=="K" or b==3) or (a=="K" or b==4) or (a=="K" or b==5) or (a=="K" or b==6) 
       or (a=="K" or b==7) or (a=="K" or b==8) or (a=="K" or b==9) or (a=="K" or b==10)
       or (a=="K" or b==2) or (a=="K" or b=="J") or (a=="K" or b=="Q")):
       print("YOU WIN")
      
       
elif((a==2 or b=="J") or (a==2 or b=="Q") or (a==2 or b=="K") or (a==2 or b=="A") 
       or (a==3 or b=="J") or (a==3 or b=="Q") or (a==3 or b=="K") or (a==3 or b=="1A")
       or (a==4 or b=="J") or (a==4 or b=="Q") or (a==4 or b=="K") or (a==4 or b=="A") 
       or (a==5 or b=="J") or (a==5 or b=="Q") or (a==5 or b=="K") or (a==5 or b=="1A")
       or (a==6 or b=="J") or (a==6 or b=="Q") or (a==6 or b=="K") or (a==6 or b=="A") 
       or (a==7 or b=="J") or (a==7 or b=="Q") or (a==7 or b=="K") or (a==7 or b=="1A")      
       or (a==8 or b=="J") or (a==8 or b=="Q") or (a==8 or b=="K") or (a==8 or b=="A") 
       or (a==9 or b=="J") or (a==9 or b=="Q") or (a==9 or b=="K") or (a==9 or b=="1A")
       or (a==10 or b=="J") or (a=="10" or b=="Q") or (a=="10" or b=="K") or (a=="10" or b=="1A")):
        print("YOU LOSS")
    
elif(a==b):
        print("Draw")

else:
        print("YOU LOSS")
