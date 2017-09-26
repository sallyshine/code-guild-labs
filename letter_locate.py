def locate(letter, word):
    index_list = []
    while True:
        try:
            index_list.append(word.index(letter))
        except ValueError:
            break
    return index_list
