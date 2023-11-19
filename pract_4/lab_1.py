num = [1, 3, 2, 4, 5, 6, 0, -5]
max_el = num.index(max(num))
min_el = num.index(min(num))

num[max_el], num[min_el] = num[min_el], num[max_el]

print(num)