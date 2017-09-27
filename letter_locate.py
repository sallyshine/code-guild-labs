"""
>>> locate('l', 'hello')
[2, 3]

>>> locate('b', 'bananas')
[0]

>>> locate('i', 'mississippi')
[1, 4, 7, 10]
"""

def locate(letter, word):
    word_list = list(word)
    index_list = []

    ind_list = []
    start = 0

    while True:
        try:
            start = word_list.index(letter, start)
            ind_list.append(start)
            start += 1
        except ValueError:
            break

    return ind_list
