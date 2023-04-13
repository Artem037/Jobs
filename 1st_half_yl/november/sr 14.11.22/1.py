import csv

displacement, team_members, passengers = input().split()
displacement, team_members, passengers = int(displacement), int(team_members), int(passengers)
with open('schooner_for_sailing.csv', encoding="utf8") as csvfile:
    reader = csv.reader(csvfile, delimiter=';', quotechar='"')
    for index, row in enumerate(reader):
        if row[0] != 'id':
            if int(row[2]) >= displacement:
                if int(row[5]) <= team_members:
                    if int(row[4]) * 2 > passengers:
                        print(f'{row[1]} ({row[3]})')
