import os
from math import ceil
os.system('cls' if os.name == '**' else 'clear')
print("So I hear you're painting a wall. Let's figure out what it is going to \
cost you.")

wall_width = int(input("What is the wall's width?\n"))
wall_height = int(input("What is the wall's height?\n"))
paint_cost = int(input("How much is a gallon of paint?\n"))
wall_sqft = wall_width * wall_height
gal_need = ceil(wall_sqft / 400)
total_cost = (gal_need * paint_cost)

print(f"It will cost ${total_cost} to paint your wall.")
