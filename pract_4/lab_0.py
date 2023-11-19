num = [1, 2, 3, 6, 11, 4, 5, 10]

result = []
for i in range(len(num)-1):
    if num[i] < num[i+1]:
        result.append(num[i+1])

print(result)