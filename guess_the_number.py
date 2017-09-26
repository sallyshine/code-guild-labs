import random
import time
import os
os.system('clear')

name = input('Hello! What is your name?\n ')
print(f"Alright, {name}. I'm thinking of a number between 1 and 100.\n")

def compare(user, computer):
    if user > computer:
        print('Sorry, your guess is too high. Try again!')
    elif user < computer:
        print('Sorry, your guess is too low. Try again!')
    else:
        print('Good job! You guessed my number in {} tries!'.format(guesses_taken))

guesses_taken = 0
computer = random.randint(1,100)

while True:
    user = int(input('Guess what number I chose:\n '))
    guesses_taken += 1
    compare(user, computer)
    if user == computer:
        time.sleep(2)
        os.system('clear')
        break
