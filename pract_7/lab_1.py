import json
import csv

files = input().split()
json_file = files[1]
csv_file = files[1].split(".")[0] + ".csv"

with open(json_file, "r") as file:
    data = json.load(file)

# json2csv.py example.json
# print(list(data.values())[0][0].values())
# print(list(data.values())[0])

with open(csv_file, "w", newline="") as file:
    writer = csv.writer(file)

    get_keys = list(data.values())[0][0].keys()
    writer.writerow(get_keys)

    for i in range(len(get_keys)):
        writer.writerow(list(data.values())[0][i].values())
