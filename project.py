import csv
import os
import random


def count_rows_and_columns(file_path):
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        header = next(reader)
        num_rows = sum(1 for _ in reader)
        num_columns = len(header)
    return num_rows, num_columns


def count_non_empty_values(file_path):
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        header = next(reader)
        counts = {}
        for field in header:
            counts[field] = {'count': 0, 'type': ''}
        for row in reader:
            for i, value in enumerate(row):
                field = header[i]
                if value.strip() != '':
                    counts[field]['count'] += 1
                    if counts[field]['type'] == '':
                        counts[field]['type'] = type(value).__name__
    return counts


def del_nan(file_path):
    temp_file = file_path + '.tmp'
    with open(file_path, 'r') as file, open(temp_file, 'w', newline='') as temp:
        reader = csv.reader(file)
        writer = csv.writer(temp)
        writer.writerow(next(reader))  # Write header
        for row in reader:
            if all(value.strip() != '' for value in row):
                writer.writerow(row)
    os.remove(file_path)
    os.rename(temp_file, file_path)


def make_ds(file_path):
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        header = next(reader)
        data = list(reader)
    random.shuffle(data)
    num_rows = len(data)
    split_index = int(num_rows * 0.7)
    learning_data = data[:split_index]
    testing_data = data[split_index:]

    base_dir = os.path.dirname(os.path.abspath(__file__))
    work_dir = os.path.join(base_dir, 'workdata')
    learning_dir = os.path.join(work_dir, 'Learning')
    testing_dir = os.path.join(work_dir, 'Testing')
    os.makedirs(learning_dir, exist_ok=True)
    os.makedirs(testing_dir, exist_ok=True)

    learning_file = os.path.join(learning_dir, 'train.csv')
    testing_file = os.path.join(testing_dir, 'test.csv')

    with open(learning_file, 'w', newline='') as learning_csv:
        writer = csv.writer(learning_csv)
        writer.writerow(header)
        writer.writerows(learning_data)

    with open(testing_file, 'w', newline='') as testing_csv:
        writer = csv.writer(testing_csv)
        writer.writerow(header)
        writer.writerows(testing_data)


# Пример использования
file_path = 'data.csv'

# Количество строк и столбцов
num_rows, num_columns = count_rows_and_columns(file_path)
print(f"Количество строк с данными: {num_rows}")
print(f"Количество колонок в таблице: {num_columns}")

# Список имен полей данных с количеством не пустых значений и типом значений
field_counts = count_non_empty_values(file_path)
for field, info in field_counts.items():
    print(f"{field}: {info['count']} {info['type']}")

# Удаление строк с пустыми полями
del_nan(file_path)
print("Строки с пустыми полями удалены.")

# Создание обучающего и тестового наборов данных
make_ds(file_path)
print("Наборы данных успешно созданы в папке 'workdata'.")
