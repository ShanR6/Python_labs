n = int(input('Введите число строк треугольника Паскаля: '))
triangle = []
for i in range(n):
    row = []
    for j in range(i + 1):
        if j == 0 or j == i:
            row.append(1)
        else:
            num = triangle[i - 1][j - 1] + triangle[i - 1][j]
            row.append(num)
    triangle.append(row)

max_width = len(str(max(triangle[-1])))

for i, row in enumerate(triangle):
    space = ' ' * (max_width // 2)
    row_str = ' '.join(space + str(num) + space for num in row)
    print(' ' * (len(triangle) - i - 1) + row_str)
