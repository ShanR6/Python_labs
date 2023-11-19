import csv
import os
import random


def Show(input_file, output_type="top", num_rows=5, separator=","):
    with open(input_file, "r") as file:
        reader = csv.reader(file, delimiter=separator)
        data = list(reader)
        if output_type == "bottom":
            data = data[-num_rows:]
        elif output_type == "random":
            data = random.sample(data, num_rows)
        elif output_type == "top":
            data = data[:num_rows]

        for row in data:
            print("|".join(row))
            print("---")


def Info(input_file, separator=","):
    with open(input_file, "r") as file:
        reader = csv.reader(file, delimiter=separator)
        data = list(reader)

        num_rows = len(data) - 1
        num_columns = len(data[0])

        print(f"Количество строк и колонок: {num_rows}x{num_columns}")

        header = data[0]
        for column_index in range(num_columns):
            column_values = [row[column_index] for row in data[1:]]
            non_empty_values = [value for value in column_values if value != ""]
            num_non_empty_values = len(non_empty_values)
            column_type = "int" if non_empty_values[0].isdigit() else "str"
            print(f"{header[column_index]} {num_non_empty_values} {column_type}")


def DelNaN(input_file, output_file_path, separator=','):
    with open(input_file, "r") as file:
        reader = csv.reader(file, delimiter=separator)
        data = list(reader)

        header = data[0]
        new_data = [header] + [row for row in data[1:] if "" not in row]
        with open(output_file_path, "w", newline="") as output_file:
            writer = csv.writer(output_file, delimiter=separator)
            writer.writerows(new_data)


def MakeDS(input_file):
    with open(input_file, "r") as file:
        reader = csv.reader(file)
        data = list(reader)

        num_rows = len(data) - 1
        num_learning_rows = int(num_rows * 0.7)

        random.shuffle(data[1:])

        learning_data = data[:num_learning_rows + 1]
        testing_data = data[num_learning_rows + 1:]

        main_dir = os.path.dirname(os.path.abspath(__file__))
        workdata_dir = os.path.join(main_dir, "workdata")
        learning_dir = os.path.join(workdata_dir, "Learning")
        testing_dir = os.path.join(workdata_dir, "Testing")

        os.makedirs(learning_dir, exist_ok=True)
        os.makedirs(testing_dir, exist_ok=True)

        learning_file_path = os.path.join(learning_dir, "train.csv")
        testing_file_path = os.path.join(testing_dir, "test.csv")

        with open(learning_file_path, "w", newline="") as learning_file:
            writer = csv.writer(learning_file)
            writer.writerows(learning_data)

        with open(testing_file_path, "w", newline="") as testing_file:
            writer = csv.writer(testing_file)
            writer.writerows(testing_data)


file_path = "example.csv"

Show(file_path, output_type="top", num_rows=5, separator=",")
Info(file_path, separator=",")
DelNaN(file_path, "non_empty.csv", separator=",")
MakeDS(file_path)
