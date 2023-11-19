num1 = [1, 2, 3, 4, 0, -2, 10, 15]
num2 = [1, 5, 4, 0, 15, 6, 3, -1]
count = 0

for i in set(num1):
    if i in num2:
        count += 1

print(f'Количество общих чисел: {count}')