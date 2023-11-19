words = ['abc', 'bcd', 'abc', 'abd', 'abd', 'dcd', 'abc']
text = ''
stat = dict()

for x in words:
    if x in stat:
        stat[x] += 1
    else:
        stat[x] = 1

for i in map(str, stat.values()):
    text += f'{i} '
else:
    if text[-1] == ' ':
        print(text[:-1])
    else:
        print(text)