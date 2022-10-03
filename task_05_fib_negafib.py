# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

a = int(input('Введите число: '))
l = []

def negafib(n):
    if n == -1:
        return 1
    elif n == -2:
        return -1
    else:
        return negafib(n + 2) - negafib(n + 1)


for i in range(-a, 0):
    l.append(negafib(i))


def fib(n):
    if n == 0:
        return 0
    elif n in [1, 2]:
        return 1
    else:
        return fib(n - 1) + fib (n - 2)

for i in range(0, a + 1):
    l.append(fib(i))
    
print(l)
