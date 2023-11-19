input = open("input.txt")
output = open("output.txt", "w")

arr = [int(num) for num in input]
input.close()

for i in sorted(arr):
    output.write(str(i) + "\n")
output.close()