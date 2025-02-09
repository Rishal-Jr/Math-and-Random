import random
options=["Rock","Paper","Scisssors"]
user_choice=input("Choose your choice: ")
computer_choice=random.choice(options)
print("You choose: ",user_choice)
print("Computer's choose: ",computer_choice)
if user_choice==computer_choice:
    print("It's a tie")
elif user_choice=="Rock" and computer_choice=="Scissors":
    print("Rock smashes the scissors. You win!")
elif user_choice=="Paper" and computer_choice=="Rock":
    print("Paper covers the Rock.You win!")
elif user_choice=="Scissors" and computer_choice=="Paper":
    print("Scissors cuts the Paper.You win!")
else:
    print("You loose")    