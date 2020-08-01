import requests
import json
import csv

damage = []

csv_file = "finalfinal.csv"

with open(csv_file, 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        if row[0] != "city":
            dam = round(float(row[3]) * float(row[5])/10000, 2)
            damage.append(dam)

# population = [1,2,3,4,5,6,7,8]

with open('damage.csv', 'w') as f:
    writer = csv.writer(f)
    for val in damage:
        writer.writerow([val])