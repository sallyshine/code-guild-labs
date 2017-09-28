"""
>>> arb(1, 2, 3, 4, 5, True, None, False, 'Python')
The 9 args are: (1, 2, 3, 4, 5, True, None, False, 'Python')

>>> arb(1, None)
The 2 args are: (1, None)


>>> stats(1, 67, 88, 44, 55, 33, 44, 22, 55, 7, 88, 9, 55, 66, 44, 33, 876)
Sum: 1587
Max: 876
Min: 1
Avg: 93
Range: 875
Entries: 17

"""
from statistics import mean
from math import floor

def arb(*args):
    print('The {} args are: {}'.format(len(args), args))

def stats(*args):
    args = list(args)
    print('Sum: {}'.format(sum(args)))
    print('Max: {}'.format(max(args)))
    print('Min: {}'.format(min(args)))
    print('Avg: {}'.format(floor(mean(args))))
    print('Range: {}'.format(abs(max(args) - min(args))))
    print('Entries: {}'.format(len(args)))
