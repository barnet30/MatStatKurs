import csv

with open('r3z1.csv') as file:
    reader = csv.reader(file)
    x1 = []
    for row in reader:
        x1.append(row[0])
name_of_x = x1[0]
x1.remove('X')
x1 = [int(val) for val in x1]

with open ('r3z2.csv') as file:
    reader = csv.reader(file)
    x2 = []
    for row in reader:
        x2.extend(row)
x2.remove('X')
x2 = [float(val) for val in x2]
