import csv
with open('all_points', "r") as f:
    for x, line in enumerate(f):
        if x >= 0:
            points = f.readlines()
print(points[0])

with open("check_element_direction_log.txt","w") as f1:
    with open("final_url_connect","r") as f:
        csvfile = csv.reader(f, delimiter=' ')
        for x, line in enumerate(csvfile):
            if x>=0:
               #49375
                a = line[0]
                b = line[1]
                c = line[2]
                num_of_element = x+1

        # pa,pb,pc are the nodes represented by x,y,z
                pa = points[int(a)]
                pb = points[int(b)]
                pc = points[int(c)]

                det = (float(pb.split()[0]) * float(pc.split()[1])) - (float(pc.split()[0]) * float(pb.split()[1])) + (float(pa.split()[0]) * float(pb.split()[1])) - (float(pb.split()[0]) * float(pa.split()[2]))
                if det < 0:
                    f1.write("problem with the element number ")
                    f1.write(str(num_of_element))
                    f1.write("\n")

with open("check_element_direction_log.txt","a") as f1:
    f1.write("checking element is done")