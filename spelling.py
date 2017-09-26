print('I-Before-E Test\n')
word = input('Give me a single English word:\n')

def ie_search(word):
    if 'cie' in word.lower():
        return False
    elif 'ie' in word.lower() or 'cei' in word.lower():
        return True
    else:
        return False

if ie_search(word) == True:
    print('{} follows the i-before-e rule!'.format(word))
else:
    print('{} does NOT follow the i-before-e rule!'.format(word))

ie_search(word)
