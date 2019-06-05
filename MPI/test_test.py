import csv
with open("data",'r') as f:
    data = f.readlines()

for x,line in enumerate(data):
    print(line)
    if x==0:
        A= float(line.split()[1]) + 23

print(A)
for r in range(1,3,1):
    print(r)

with open('data','r') as f:
    p2 = f.readlines()
csvf = csv.reader(p2,delimiter = ' ')

for x,line in enumerate(csvf):
    if x ==1:
        print(line[1])