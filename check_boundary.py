with open("boundary_points1","w") as f3:
    with open("all_points","r") as f2:
        for y, row in enumerate(f2):
            with open("new_boundary","r") as f:
                for x,line in enumerate(f):
                    num = int(line.split()[11])
                    if y == num:
                        f3.write(row)


with open("boundary_points2","w") as f3:
    with open("all_points","r") as f2:
        for y, row in enumerate(f2):
            with open("NEW_GEO.cli","r") as f:
                for x,line in enumerate(f):
                    num = int(line.split()[11])
                    if y == num:
                        f3.write(row)

with open("boundary_points1","r") as f:
    bp = f.read()

with open("boundary_points2","r") as f2:
    for x ,line in enumerate(f2):
        if line not in bp :
            print(line)
            print(x+1)