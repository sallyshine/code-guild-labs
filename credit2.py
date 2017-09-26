cc_num = input('Enter 16-digit credit card number:\n')
cc_num = list(cc_num)
print(cc_num)

check_digit = cc_num[-1]
new_cc1 = cc_num[:-1]
print(new_cc1)

new_cc1.reverse()
print(new_cc1)

new_cc2 = []

for num in range(len(new_cc1)):
    if num % 2 == 0:
        new_cc2.append(int(new_cc1[num])*2)
    else:
        new_cc2.append(int(new_cc1[num]))

print(new_cc2)

new_cc3 = []

for num2 in new_cc2:
    if num2 > 9:
        num3 = (num2 - 9)
        new_cc3.append(num3)
    else:
        new_cc3.append(num2)

print(new_cc3)

new_cc3 = sum(new_cc3)
print(new_cc3)

new_cc3 = str(new_cc3)
new_cc3 = list(new_cc3)

if check_digit == new_cc3[1]:
    print('Valid!')
else:
    print('Invalid!')
