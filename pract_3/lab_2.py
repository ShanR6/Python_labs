text = input('Введите строку: ')
t = ([(text.count(i), i) for i in text if i != ' '])
print(sorted(set(t))[::-1][:3])
