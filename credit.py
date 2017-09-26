def check_digit(n):
    check_digit = n[-1]

def new_cc_num(card):
    new_cc_num = card[:-1]
    print(new_cc_num)

def reverse(num):
    num.reverse()
    print(num.reverse())

def double(cc):
    for n in cc:
        new_cc = cc[::2] * 2
        print(new_cc)

def subtract_nine(card_num):
    card_num = int(card_num)
    for num in card_num:
        if num >= 9:
            new_num = num - 9
            card_num.append(new_num)
        else:
            card_num.append(num)
    print(card_num)

def sum_list(num_list):
    num_list = int(num_list)
    num_list2 = sum(num_list)
    print(num_list2)

while True:
    cc_num = input('Enter 16-digit credit card number:\n')
    cc_num = list(cc_num)
    print(cc_num)
    digit_check = check_digit(cc_num)
    new_cc2 = new_cc_num(cc_num)
    new_cc4 = double(new_cc3)
    new_cc5 = subtract_nine(new_cc4)
    cc_sum = sum_list(new_cc5)
    print(str(cc_sum)[1])
    if digit_check == int(str(cc_sum)[1]):
        print('Valid!')
        break
    else:
        print('Not valid!')
        break
