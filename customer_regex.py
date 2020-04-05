import csv
import re
data = []

with open('customerData.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        data.append(row)
print(data[0])
print(data[1]["Name"])
print(data[2]["Spent Past 30 Days"])