import random
import os
os.system('clear')

num_dice = int(input("Let's roll some dice! How many dice do you want to roll?\n"))
num_sides = int(input("How many sides per die?\n"))

print("Let's roll... ")
for d in range(num_dice):
    print(random.randint(1, num_sides))
