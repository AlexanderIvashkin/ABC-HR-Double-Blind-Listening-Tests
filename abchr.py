import csv

with open('ABC1.csv', newline='') as test_description:
    csvreader = csv.reader(test_description, delimiter=';', quotechar='"')
    for z in csvreader:
        for i in z:
            print(i)
