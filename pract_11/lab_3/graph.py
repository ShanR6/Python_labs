import csv
import matplotlib.pyplot as plt

with open("passengers.csv", "r") as file:
    reader = csv.reader(file)
    next(reader)
    data = list(reader)

years = [row[0] for row in data]
passengers = [int(row[1]) for row in data]

plt.plot(years, passengers)
plt.xticks([])
plt.xlabel("Год-месяц")
plt.ylabel("Количество пассажиров")
plt.title("Пассажиропоток")

plt.show()
