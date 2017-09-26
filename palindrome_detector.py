user_word = input("Enter a word/sentence for testing: \n")
word = user_word.lower()
word2 = word.replace(" ", "")

word_list = list(word2)

def palindrome(word):
    if word_list[::] == word_list[::-1]:
        return True
    else:
        return False


if palindrome(word) == True:
    print(f"{user_word} is a palindrome!")
else:
    print(f"{user_word} is not a palindrome!")
