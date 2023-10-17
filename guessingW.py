import random
name=input("What is your name? ")
print("Good luck ",name," ! ")
words=['rainbow','computer','python','science','programming','mathematics','player',
        'condition','water','board','reverse']
word=random.choice(words)
print("Guess the character")
guesses=''
turns=15
while turns>0:
    failed=0
    for char in word:
        if char in guesses:
            print(char,end=" ")
        else:
            print("_")
            failed+=1
    if failed==0:
        print("\n\tYOU WIN")
        print("\tThe word is ",word)
    print()
    guess=input("Guess a character: ")
    guesses+=guess
    if guess not in word:
        turns-=1
        print("Wrong")
        print("You have ",+turns," more guesses ")
        if turns==0:
            print("YOU LOSS")