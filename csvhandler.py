import csv


def write(text):
    with open('ids.csv','w') as file:
        csv_writer = csv.writer(file)
        csv_writer.writerow([text])


def read():
    with open('ids.csv', 'r') as file:
        csv_reader = csv.reader(file)
        return [row[0] for row in csv_reader if row]
