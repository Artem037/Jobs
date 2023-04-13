import csv


with open('dead_mans_chest.csv', encoding="utf8") as csvfile:
    reader = csv.DictReader(csvfile, delimiter=';', quotechar='"')

for record in reader:
    print(record)