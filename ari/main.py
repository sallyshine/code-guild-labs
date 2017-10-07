from textstat.textstat import textstat

ari_scale = {
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


text = "In plain English, the score is computed by multiplying the number of \
    characters divided by the number of words by 4.17, adding the number of \
    words divided by the number of sentences multiplied by 0.5, and subtracting \
    21.43. If the result is a decimal, always round up."

print(textstat.automated_readability_index(text))
# new_text = ''
# chars = len(text)
# for ch in range(chars):
#     if text[ch] == '.':
#         if text[ch-1].isnumeric() and text[ch+1].isnumeric:
#             pass
#         else:
#             new_text += text[ch]
#     else:
#         new_text += text[ch]
#
# words_list = new_text.split(' ')
# sentences = len([s for s in new_text.split('.') if len(s) > 0])
# ari = (chars / len(words_list)) * 4.71 + (len(words_list) / sentences) * 0.5 - 21.43

# print(text)


# def get_ari(text):
#     # new_text = text.replace(".", "").replace(",", "").replace("?", "").replace('"', "")\
#     # .replace("!", "").replace("-", "").replace(":", "").replace(";", "").lower().split()
#     text = text.lower().replace('\n', '')
#
#     for p in string.punctuation:
#         text = text.replace(p, "")
#     text = text.split()
#     word_count = dict()
#     for word in text:
#         if word not in word_count:
#             word_count[word] = 1
#         else:
#             word_count[word] += 1
#     word_count = sorted(word_count.items(), key=itemgetter(1), reverse=True) [:10]
#     for key, value in word_count:
#         print('{} {}'.format(key, value))
