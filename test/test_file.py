l = [1,2,3,4,5,6]
the_file = "/Users/MahdiMoslemi/Desktop/PycharmProjects/test/data2"
with open(the_file , 'r') as file:
    for i, line in enumerate(file):
        if (set(list(map(int, line.split()))).issubset(l)):
            print("Line %d has all numbers from the list" % i)

