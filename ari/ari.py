import glob #gets back a list of files that follow a pattern
import re #regular expressions is a tool used for parsing text
import os

ARI_SCALE = {
     1: {'ages':   '5-6', 'grade_level': 'Kindergarten'},
     2: {'ages':   '6-7', 'grade_level':    '1st Grade'},
     3: {'ages':   '7-8', 'grade_level':    '2nd Grade'},
     4: {'ages':   '8-9', 'grade_level':    '3rd Grade'},
     5: {'ages':  '9-10', 'grade_level':    '4th Grade'},
     6: {'ages': '10-11', 'grade_level':    '5th Grade'},
     7: {'ages': '11-12', 'grade_level':    '6th Grade'},
     8: {'ages': '12-13', 'grade_level':    '7th Grade'},
     9: {'ages': '13-14', 'grade_level':    '8th Grade'},
    10: {'ages': '14-15', 'grade_level':    '9th Grade'},
    11: {'ages': '15-16', 'grade_level':   '10th Grade'},
    12: {'ages': '16-17', 'grade_level':   '11th Grade'},
    13: {'ages': '17-18', 'grade_level':   '12th Grade'},
    14: {'ages': '18-22', 'grade_level':      'College'}
}

def get_book_data_from_list():
    books = glob.glob(f'{ os.getcwd() }/books/*.txt')

    for index, book in enumerate(books):
        filename = book.split("/")[-1]
        print(f'{index}: {filename}')

    book_selection = int(input("Pick a book by #: \n"))
    book = books[book_selection]

    with open(book, 'r') as f:
        return f.read()

if __name__ == '__main__':
    data = get_book_data_from_list()

    sentences = re.split(r'\.+|\!+|\?+|;|:', data)
    sentences = [sentence.strip() for sentence in sentences]

    words = re.split(r'\n+|\ +|\t+|\-+', data)

    characters = sum(len(word) for word in words)

    score = 4.71 * (characters / len(words)) + 0.5 * (len(words) / len(sentences)) - 21.43

    score = round(score)

    print(score)
    print(ARI_SCALE[score])









# with open('pride_prejudice.txt', 'r', encoding='utf-8') as f:
#     text = f.read()
