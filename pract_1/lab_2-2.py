n = int(input('Введите число: '))

for i in range(1, n + 1):
    row = ''
    for j in range(1, i + 1):
        row += str(j)
    for j in range(i - 1, 0, -1):
        row += str(j)
    print(row.center(n * 2 - 1))
