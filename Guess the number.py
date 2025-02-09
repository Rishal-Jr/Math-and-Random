import random
playing=True
number=str(random.randint(10,20))

print("I will generate a number between 10 to 20, And you have to guess it.")
print("The game will continue untill you get 1 here!")

while playing:
    guess=int(input("Input the best guess:  \n"))
    if guess==number:
        print("You guessed the number correctly!")
        print("You won!")
    else:
        print("Your guess is not quite right. Try again!")