import csv


with open ('r3z2.csv') as file:
    reader = csv.reader(file)
    x2 = []
    for row in reader:
        x2.extend(row)
x2.remove('X')
x2 = [float(val) for val in x2]
