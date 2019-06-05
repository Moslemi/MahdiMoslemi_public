import csv
import operator
with open('/Users/MahdiMoslemi/Desktop/PycharmProjects/Triangular/CollectNodes', 'r') as sample:
    csv1 = csv.reader(sample, delimiter=' ')
    sort = sorted(csv1 , key = operator.itemgetter(1))

with open('/Users/MahdiMoslemi/Desktop/PycharmProjects/Triangular/CollectNodes2', 'w') as f:
    f.write(str(sort))
