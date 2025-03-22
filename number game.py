import random
playing = True
number = str(random.randint(10.30))

print("i will generate a number from 0 to 9,and you have to giess the number on digit at a time,")
print("the game ends when you get one")

while playing:
    guess = imput("give me your best guess")
    if number == guess:
        print("you win the game")
        print("the number was",number)
        break
    else:
        print("your guess isn't quite right,try again")