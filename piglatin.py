print("Let's play a word game!")

user_word = input("Give me a single English word: \n")
word = user_word.lower()
first_letter = word[0]
pig = "ay"
pig2 = "yay"

if len(user_word) > 0 and user_word.isalpha():
    if first_letter in 'aeiou':
        new_word = word + pig2
        print(f"{user_word} in Pig Latin is {new_word}!")
    else:
        word = user_word.lower()
        new_word = word + first_letter + pig
        new_word = new_word[1:len(new_word)]
        print(f"{user_word} in Pig Latin is {new_word}!")
