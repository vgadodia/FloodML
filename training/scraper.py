import requests
import datetime

def get_data(date, month, year, days, location):
    a = datetime.date(year, month, date)
    b = a - datetime.timedelta(days)
    
    k = "https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/weatherdata/history?&aggregateHours=" + str(24 * days) + "&startDateTime=" + str(b) + "T00:00:00&endDateTime=" + str(a) + "T00:00:00&unitGroup=uk&contentType=json&dayStartTime=0:0:00&dayEndTime=0:0:00&location=" + location + ",India&key=QG54K69BV36JZ7G6FD46BBY57"
    x = requests.get(k).json()['locations']
    
    for i in x:
        y = x[i]

    y = y['values'][0]
    final = [y['temp'], y['maxt'], y['wspd'], y['cloudcover'], y['precip'], y['humidity'], y['precipcover']]

    return final

states = ['Karnataka', 'Gujarat', 'Rajasthan', 'Maharashtra', 'Madhya Pradesh']
import csv
import random
f = open('data1.csv', mode='w', newline = '')
writer = csv.writer(f, delimiter=',')


for i in states:
    for j in range(1, 31):
        a = random.randint(1, 28)
        b = random.randint(1, 12)
        c = random.randint(2013, 2019)

        k = get_data(a, b, c, 15, i)

        if k[4] != None:
            if k[4] < 20:
                print(k)
                print(j)
                writer.writerow(k + [0])



def extract_date(x):
    k = x.split(" ")

    a = int(k[0])

    d = {'january':1, 'february':2, 'march':3, 'april':4, 'may':5, 'june':6, 'july':7, 'august':8, 'september':9, 'october':10, 'november':11, 'december':12}
    b = d[k[1][0:len(k[1]) - 1].lower()]

    c = int(k[2])

    return [a, b, c]

def process(k):
    x = extract_date(k[1])

    return get_data(x[0], x[1], x[2], 15, k[0])


f = open('data.csv', mode='w', newline = '')
writer = csv.writer(f, delimiter=',')

with open('mined.csv', mode='r') as csv_file:
    csv_reader = csv.reader(csv_file)
    
    for row in csv_reader:
        print(row)
        
        writer.writerow(process(row) + [1])



