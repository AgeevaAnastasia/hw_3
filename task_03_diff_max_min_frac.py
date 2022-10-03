# Задайте список из вещественных чисел. 
# Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19             (5 - это 5.00, но её не берём, у неё как бы нет дробной части)

# l = [float(x) for x in input('Введите вещественные числа в список через пробел: ').split(' ')]
l = [1.1, 1.2, 3.1, 5, 10.01]
print(l, end = ' ')

for i in range(len(l)):
    l[i] = round((l[i] % 1), 15)


def find_max(nums):
    max_num = nums[0]
    for i in nums:
        if i > max_num:
            max_num = i
    return max_num


def find_min(nums):
    min_num = nums[0]
    for i in nums:
        if i == 0:
            i = 100
        if i < min_num:
            min_num = i
    return min_num


max_number = find_max(l)
min_number = find_min(l)
result = max_number - min_number
print(f'=> {result}')
