# Task 1
'''
print('Введите числа:')
a, b, c = float(input()), float(input()), float(input())

if a == b == c:
    print(3)
elif a == b or a == c or b == c:
    print(2)
    if a > b and a > c:
        print(a, '- минимальное число')
    elif b > a and b > c:
        print(b, '- минимальное число')
    else:
        print(c, '- минимальное число')
else:
    print(0)
    if a > b and a > c:
        print(a, '- минимальное число')
    elif b > a and b > c:
        print(b, '- минимальное число')
    else:
        print(c, '- минимальное число')
'''

# Task 2.1
'''
n = int(input())
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, sep='', end='')
    print()
'''

# Task 2.2
def print_pyramid(n):
    max_num_digits = len(str(n))  # Максимальное количество разрядов чисел в треугольнике
    width = n * (max_num_digits + 1) - 1  # Определяем ширину строки

    for i in range(1, n+1):
        row = ''
        for j in range(1, i+1):
            row += str(j).rjust(max_num_digits)  # Добавляем числа от 1 до i с выравниванием по разрядам
        for j in range(i-1, 0, -1):
            row += str(j).rjust(max_num_digits)  # Добавляем числа обратно от i-1 до 1 с выравниванием по разрядам
        print(row.center(width))

# Запрашиваем у пользователя число n
n = int(input("Введите число n: "))

# Выводим равнобедренный треугольник
print_pyramid(n)
