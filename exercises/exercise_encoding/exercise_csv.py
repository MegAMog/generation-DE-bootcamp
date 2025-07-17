import csv

with open('ford_escort.csv', 'r') as file:
    reader = csv.reader(file, delimiter=',')
    for idx, row in enumerate(reader):
        if idx!=0:
            print(row) 
            print(type(row))

# with open('ford_escort.csv', 'r') as file:
#     reader = csv.DictReader(file, delimiter=',')
#     for row in reader:
#         print(row)