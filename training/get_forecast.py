import csv
import datetime
import pickle
import requests

def get_data(lat, lon):
    
    
    k = f"https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{lat},{lon}?include=fcst%2Cobs%2Chistfcst%2Cstats%2Cdays%2Chours%2Ccurrent%2Calerts&key=THPF54ER75KGFFAXVPU52235Q&options=beta&contentType=json"
    x = requests.get(k).json()['locations']
    for i in x:
        y = x[i]['values']

    final = [0, 0, 0, 0, 0, 0]

    for j in y:
        final[0] += j['temp']
        if j['maxt'] > final[1]:
            final[1] = j['maxt']
        final[2] += j['wspd']
        final[3] += j['cloudcover']
        final[4] += j['precip']
        final[5] += j['humidity']
    final[0] /= 15
    final[2] /= 15
    final[3] /= 15
    final[5] /= 15

    return final

def testConnection():
    return "yo"



f = open('cities.csv', 'r', encoding='UTF-8')
ff = open('plotting.csv', mode='w', newline = '')
writer = csv.writer(ff, delimiter=',')

r = csv.reader(f)

for row in r:
    print(row)
    writer.writerow(get_data(row[1], row[2]))