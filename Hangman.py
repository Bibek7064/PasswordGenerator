import random
import time
lst=["python","secret","major","temp","project","password", "hitman"]
name = input("What is your name? ")
print("Hello, " + name, "Time to play hangman!")
print("")
time.sleep(1)
print("Start guessing...")
time.sleep(0.5)
guesses = ''
j=1
while j==1:
    word=lst[random.randint(0,6)]
    turns = 10
    guesses = ''
    while turns > 0:
        failed = 0
        for char in word:
            if char in guesses:
                print(char)
            else:
                print("_")
                failed += 1
        if failed == 0:
            print("You won")
            break
        print('')
        guess = input("guess a character:")
        guesses += guess
        if guess not in word:
            turns -= 1
            print("Wrong")
        print("You have", + turns, 'more guesses')
        if turns == 0:
            print("You Lose")
    choice=(input("Do you want to continue(Y/N)")).upper()
    if choice=="N":
       if turns==0:
           print("You should have tried again to make it right")
           break
       else:
           print("Well played !")
           break

