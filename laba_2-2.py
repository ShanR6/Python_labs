n = int(input('Введите число: '))
triangle = ['*']
if n <= 1:
    for i in range(1):
        space = ' ' * (2 ** i)
        result = []
        for line in triangle:
            result.append(space + line + space)
        for line in triangle:
            result.append(line + ' ' + line)
        triangle = result
else:
    for i in range(n):
        space = ' ' * (2 ** i)
        result = []
        for line in triangle:
            result.append(space + line + space)
        for line in triangle:
            result.append(line + ' ' + line)
        triangle = result

for line in triangle:
    print(line)
