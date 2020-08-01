def process(k):
    final = ""

    for i in k:
        if i == "ā":
            final += "a"
        elif i == "ē":
            final += "e"
        elif i == "ī":
            final += "i"
        elif i == "ō":
            final += "o"
        elif i == "ū":
            final += "u"
        else:
            final += i
    return final

import csv

f = open('final_plot.csv', 'r', encoding='UTF-8')
ff = open('finalfinal.csv', mode='w', newline = '', encoding = "UTF-8")
writer = csv.writer(ff, delimiter=',')

reader = csv.reader(f)

for i in reader:
    writer.writerow([process(i[0])] + i[1::])