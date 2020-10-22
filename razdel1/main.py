from razdel1.read_csv import data, sample
#import pandas as pd

sample_size = data['X'].count()
print("Объём выборки: "+str(sample_size))

#print(read_csv.data['X'].value_counts())

sample_max = data['X'].max()
print("Максимум выборки: "+str(sample_max))

sample_min = data['X'].min()
print("Минимум выборки: "+str(sample_min))

sample_range = sample_max - sample_min
print("Размах выборки = " + str(sample_range))

sample_mean = data['X'].sum()/data['X'].count()
print("Математическое ожидание = " + str(round(sample_mean,3)))

sample_moved_dispersion = 0.0
for elem in sample:
    sample_moved_dispersion += (elem - sample_mean) * (elem - sample_mean)
sample_moved_dispersion = sample_moved_dispersion/sample_size
print("Выборочная смещённая дисперсия = "+str(round(sample_moved_dispersion,3)))

sample_not_moved_dispersion = sample_moved_dispersion * sample_size / (sample_size-1)
print("Выборочная несмещённая дисперсия = "+str(round(sample_not_moved_dispersion,3)))

sample_diviation = sample_moved_dispersion ** 0.5
print("Стандартное отклонение = "+str(round(sample_diviation,3)))

sample_asymmetry = 0.0
for elem in sample:
    sample_asymmetry += ((elem - sample_mean) ** 3)
sample_asymmetry = sample_asymmetry / sample_size / (sample_diviation**3)
print("Асимметрия = " + str(round(sample_asymmetry,3)))

sample_median = 0
sample.sort()
if (sample_size - 1) % 2 ==0:
    sample_median = sample[(sample_size - 1)/2 + 1]
else:
    sample_median = (sample[(sample_size - 1)//2 + 1] +
                     sample[(sample_size - 1)//2 + 2])/2
print("Медиана = " + str(sample_median))

sample_up_quartile = 0
sample_down_quartile = 0
if (sample_size - 1) * 0.25 == int((sample_size - 1) * 0.25):
    sample_down_quartile = sample[int((sample_size - 1)*0.25) + 1]
else:
    sample_down_quartile = (sample[int((sample_size - 1) *0.25) + 1] +
                     sample[int((sample_size - 1) *0.25) + 2]) / 2
if (sample_size - 1) * 0.75 == int((sample_size - 1) * 0.75):
    sample_up_quartile = sample[int((sample_size - 1)*0.75) + 1]
else:
    sample_up_quartile = (sample[int((sample_size - 1) *0.75) + 1] +
                     sample[int((sample_size - 1) *0.75) + 2]) / 2

print("Интерквартильная широта = " +
      str(sample_up_quartile - sample_down_quartile))

