n = int(input('Введите число:'))
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, sep='', end='')
    print()


n = int(input('Введите число:'))
curString = ''
for i in range(1, n + 1):
    curString += str(i) + ''
    print(curString)
