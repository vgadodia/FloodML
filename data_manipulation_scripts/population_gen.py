import requests
import json
import csv

population = []

def get_city_opendata(city, country):
    tmp = 'https://public.opendatasoft.com/api/records/1.0/search/?dataset=worldcitiespop&q=%s&sort=population&facet=country&refine.country=%s'
    cmd = tmp % (city, country)
    res = requests.get(cmd)
    dct = json.loads(res.content)
    out = dct['records'][0]['fields']
    return out

csv_file = "finalfinal.csv"

with open(csv_file, 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        if row[0] != "city":
            # print(row[0])
            try:
                pop = get_city_opendata(row[0], 'in')
                population.append(pop["population"])
            except:
                population.append(0)

# population = [1,2,3,4,5,6,7,8]

with open('pop.csv', 'w') as f:
    writer = csv.writer(f)
    for val in population:
        writer.writerow([val])