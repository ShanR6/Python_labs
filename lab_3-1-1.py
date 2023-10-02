text = 'Y4g2ke3A3BV'
length = len(text)

result = ''
for i in range(length - 1):
    if text[i + 1].isdigit():
        result += text[i] * int(text[i + 1])
    elif not text[i].isdigit():
        result += text[i]
else:
    if not text[-1].isdigit():
        result += text[-1]

print(result)
