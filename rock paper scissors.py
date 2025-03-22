import random
options = {"rock","paper","scissors"}
user_choice = input("choose rock, paper ,or scissors:")
computer_choice = random.choice(options)
print("you choice", user_choice)
print("computer chose:",computer_choice)

if user_choice == computer_choice:
    print("It's tie!")
elif user_choice == "rock" and computer_choice == "scissors":
 print("rocksmashes scissors! you win!")
elif user_choice == "paper" and computer_choice =="rock":
   print("paper covers rock you win")
elif user_choice == "scissors" and computer_choice =="paper":
   print("scissors cut paper! you win!")
else:
   print("you lose!.")