print('Введите числа:')
a, b, c = float(input()), float(input()), float(input())

if a == b == c:
    print(3)
elif a == b or a == c or b == c:
    print(2)
else:
    print(0)
