text = 'YYYYggkeeeAAABV'

length = len(text)
count = 1
result = ''
for i in range(length-1):
    if text[i] == text[i + 1]:
        count += 1
    else:
        if count == 1:
            result += text[i]
        else:
            result += f'{text[i]}{count}'
        count = 1
else:
    if text[-1] not in result:
        result += text[-1]

print(result)
