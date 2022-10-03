# Напишите программу, которая будет преобразовывать десятичное число в двоичное.

# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

a = int(input('Введите число в десятичной системе: '))

l = []

def dec_to_bin(num):
    if num == 0:
        return l
    else:
        l.append(num % 2)
        dec_to_bin(num // 2)
    


dec_to_bin(a)
l = l[::-1]

print(f'{a} -> ', end = '')
for i in l:
    print(i, end = '')

