import csv

with open('r2z1.csv') as file:
    reader = csv.reader(file)
    x = []
    y = []
    for row in reader:
        x.append(row[0])
        y.append(row[1])
name_of_x = x[0]
name_of_y = y[0]
x.remove('X')
y.remove('Y')
x = [float(val) for val in x]
y = [float(val) for val in y]


with open ('r2z2.csv') as file:
    reader = csv.reader(file)
    sample = []
    for row in reader:
        sample.extend(row)
sample.remove('X')
sample = [float(val) for val in sample]

