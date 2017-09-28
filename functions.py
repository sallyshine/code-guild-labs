"""

>>> combine(7, 4)
11

>>> combine(42)
42

>>> combine_many(980, 667, 4432, 788, 122, 9, 545, 222)
7765

>>> choose_longest("Greg", "Rooney")
'Rooney'

>>> choose_longest("Greg", "Rooney", "Philip", "Maximus", "Gabrielle")
'Gabrielle'

>>> choose_longest("Greg", [0, 0, 0, 0, 4])
[0, 0, 0, 0, 4]

"""

def combine(num, num2=0):
    total = num + num2
    return total

def combine_many(*args):
    return sum(args)

def choose_longest(*args):
    longest = None
    cur_len = 0
    for item in args:
        if len(item) > cur_len:
            cur_len = len(item)
            longest = item
    return longest
