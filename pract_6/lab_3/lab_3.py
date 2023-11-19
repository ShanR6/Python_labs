input = open("input.txt", encoding="utf-8")
arr = input.readlines()
input.close()

new_arr = sorted(arr, key=lambda child: int(child.split()[-1]))
num_arr = sorted([int(i.split()[-1]) for i in new_arr])
num_iter = (num_arr.count(num_arr[0]), num_arr.count(num_arr[-1]))

with open("junior.txt", "w", encoding="utf-8") as file:
    for i in range(num_iter[0]):
        file.write(new_arr[i].rstrip() + "\n")

with open("senior.txt", "w", encoding="utf-8") as file:
    for i in range(num_iter[1]):
        file.write(new_arr[-1-i].rstrip() + "\n")