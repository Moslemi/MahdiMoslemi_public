import csv

with open("test_parameters","r") as f:
    csvf = csv.reader(f , delimiter = ' ')
    for x,line in enumerate(csvf ):
        if x==0:
            topol = line
            print(topol[0])
