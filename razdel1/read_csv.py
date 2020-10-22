import csv
import pandas as pd


with open('C:/Users/barnet/PycharmProjects/kursMatStat/r1z1.csv') as file:
    reader = csv.reader(file)
    sample = []
    for row in reader:
        sample.extend(row)
name_of_random_value = sample[0]
sample.remove('X')
sample = [float(value) for value in sample]


data = pd.read_csv('C:/Users/barnet/PycharmProjects/kursMatStat/r1z1.csv')


