# Pursued by the Empire's sinister agents, Princess Leia races home
# aboard her starship, custodian of the stolen plans that can save
# her people and restore freedom to the galaxy...

print("Let's play a game! \nGive me an answer to the following questions:\n")

neg_char = input('A negative personality characteristic?\n')
name = input('A female name?\n')
vehicle = input('A type of transportation vehicle?\n')
place = input('A place?\n')

madlib = f"""
Pursued by the Empire's {neg_char} agents,
Princess {name} races home aboard her {vehicle},
custodian of the stolen plans that can save
her people and restore freedom to {place}..."
"""

print(madlib)
