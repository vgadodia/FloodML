import csv
import pickle

model = pickle.load(open('model.pickle', 'rb'))
c = open('cities.csv', 'r', encoding='UTF-8')

cr = csv.reader(c)

cities = []

for c_row in cr:
    cities.append(c_row) 

d = open('plotting.csv', 'r', encoding='UTF-8')

dr = csv.reader(d)

forecast = []
for d_row in dr:
    k = list(map(float, d_row))
    forecast.append([k[4], model.predict([k])[0]])

ff = open('final_plot.csv', mode='w', newline = '', encoding="UTF-8")
writer = csv.writer(ff, delimiter=',')

for i in range(0, len(forecast)):
    writer.writerow(cities[i] + forecast[i])
print(forecast)


