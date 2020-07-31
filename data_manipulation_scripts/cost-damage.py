import requests
import json
import csv

cost = []

csv_file = "finalfinal.csv"

with open(csv_file, 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        if row[0] != "city":
            dam = int(float(row[6]) * 500)
            cost.append(dam)

# population = [1,2,3,4,5,6,7,8]

with open('cost.csv', 'w') as f:
    writer = csv.writer(f)
    for val in cost:
        writer.writerow([val])