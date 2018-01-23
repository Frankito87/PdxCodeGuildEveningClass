import datetime

date = datetime.datetime.strptime('25-MAR-2016', '%d-%b-%Y')
print(date.year)
print(date.month)
print(date.day)


def load_file():
    with open('rain_table.txt', 'r') as f:
        lines = f.readlines()

    start_line = 0
    while '----' not in lines[start_line]:
        start_line += 1
    start_line += 1

    print(start_line)

    data = []
    for i in range(start_line, len(lines)):
        data_line = lines[i].split()
        date = datetime.datetime.strptime(data_line[0], '%d-%b-%Y')
        daily_rainfall = int(data_line[1]) if data_line[1] != '-' else None
        data.append((date, daily_rainfall))

    return data


data = load_file()
print(data)
