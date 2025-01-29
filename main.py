import csv


def read_csv(filename):
    raw_data = dict()
    with open(filename, 'r') as in_file:
        reader = csv.reader(in_file, quotechar='"', delimiter=',', skipinitialspace=True)
        for row in reader:
            raw_data[row[0]] = row[1:]
    return raw_data


def read_names(filename):
    with open(filename, 'r') as in_file:
        return [name.strip() for name in in_file]


def write_csv(filename, data, include_names=True):
    with open(filename, 'w') as out_file:
        writer = csv.writer(out_file, quotechar='"', delimiter=',', quoting=csv.QUOTE_MINIMAL)
        for name, values in data.items():
            if include_names:
                writer.writerow([name] + values)
            else:
                writer.writerow(values)


def replace(data, index, condition, new_value):
    for values in data.values():
        if condition(values[index]):
            values[index] = new_value


def main():
    names = read_names('names.txt')
    raw_data = read_csv('canvas_grades.csv')
    columns = [6]  # 0 is the column AFTER the name column
    filtered_data = {name: [raw_data[name][i] for i in columns] for name in names}

    replace(filtered_data, 0, lambda x: x == '0.00', 'nok')
    replace(filtered_data, 0, lambda x: x == '1.00', 'ok')
    # replace(filtered_data, 1, lambda x: x == '0.00', 'nok')
    # replace(filtered_data, 1, lambda x: x == '0.75', '4')
    # replace(filtered_data, 1, lambda x: x == '1.00', '5')

    write_csv('processed_data.csv', filtered_data, include_names=True)


if __name__ == '__main__':
    main()
