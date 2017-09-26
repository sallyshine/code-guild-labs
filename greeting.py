print("Hello there! ")

user_name = input("What is your name?\n")
user_age = input("How old are you?\n")
# users age will be received as a string, so convert to int to add 1.
user_age2 = int(user_age) + 1

print("*" * len(user_name))

greeting = f"Wow {user_name}, that means next year you will be {user_age2}! \
Not going to lie, that's kind of old."

print(greeting)
