"""

>>> a = 'music'
>>> b = [17, 28, 42, 31, 12]

>>> display_indexes(a)
m 0
u 1
s 2
i 3
c 4


>>> parallel(a, b)
m 17
u 28
s 42
i 31
c 12

"""
a = 'music'
b = [17, 28, 42, 31, 12]

def display_indexes(word):
    for letter in word:
        print(letter, str(word.index(letter)))

def parallel(list1, list2):
    for i in list1:
        item = list1.index(i)
    for o in list2:
        obj = list2.index(o)
    while item == obj:
        print(i, o)

print(parallel(a, b))
