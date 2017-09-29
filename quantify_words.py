from operator import itemgetter
import string

def quantify_words(text):
    # new_text = text.replace(".", "").replace(",", "").replace("?", "").replace('"', "")\
    # .replace("!", "").replace("-", "").replace(":", "").replace(";", "").lower().split()
    text = text.lower().replace('\n', '')

    for p in string.punctuation:
        text = text.replace(p, "")
    text = text.split()
    word_count = dict()
    for word in text:
        if word not in word_count:
            word_count[word] = 1
        else:
            word_count[word] += 1
    word_count = sorted(word_count.items(), key=itemgetter(1), reverse=True) [:10]
    for key, value in word_count:
        print('{} {}'.format(key, value))

# with open('pride_prejudice.txt', 'r', encoding='utf-8') as word:
#     words = word.read()
#
# quantify_words(words)
