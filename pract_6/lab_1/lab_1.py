input = open("input.txt")
output = open("output.txt", "w")
count = 1

arr = map(int, input.readline().split())
input.close()

for x in arr:
    count *= x

output.write(str(count))
output.close()