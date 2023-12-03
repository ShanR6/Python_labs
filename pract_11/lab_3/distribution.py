import csv
import matplotlib.pyplot as plt

with open("passengers.csv", "r") as file:
    reader = csv.reader(file)
    next(reader)
    data = list(reader)

months = []
passengers = []
for row in data:
    year_month = row[0].split("-")
    year = int(year_month[0])
    month = int(year_month[1])
    if 1951 <= year <= 1955:
        months.append(month)
        passengers.append(int(row[1]))

plt.hist(months, bins=12, range=(1, 12), weights=passengers)
plt.xticks([*range(1, 13)])
plt.xlabel("Месяц")
plt.ylabel("Количество пассажиров")
plt.title("Распределение пассажиров по месяцам в 1951-1955 гг.")

plt.show()
