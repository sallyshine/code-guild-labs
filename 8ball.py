import random
print('Welcome to the Magic 8 Ball!')

question = input('Type your question below:\n ')
prediction = ['Outlook not good', 'Try again later', 'It\'s your lucky day!', 'Nope... not today!', 'Yessssss!']
print(random.choice(prediction))

yes = True

while yes:
    question2 = input('Do you have another question?\n ')
    if question2 in ['yes', 'y']:
        question = input('Type another question below:\n ')
        print(random.choice(prediction))
    elif question2 in ['no', 'n']:
    yes = False
    print('Goodbye!')
