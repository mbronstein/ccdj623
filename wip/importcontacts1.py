import csv
import json
import os

print(os.getcwd())
csvfile = open('asc.csv', 'r')
jsonfile = open('ascontacts.json', 'w')

fieldnames = ("Name","address","city","state","zip","email","phone")
reader = csv.DictReader( csvfile, fieldnames)
for row in reader:
    json.dump(row, jsonfile)
    jsonfile.write('\n')