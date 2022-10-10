import csv
with open('biostats.csv','r') as csv_file:
    f = csv.reader(csv_file)
    for cf in f:
        print(cf)