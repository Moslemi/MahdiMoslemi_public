new_points = "points_lidar"

def sum_points(all_points , GEO_t3s):

    #all_points = "all_points"
    #GEO_t3s = '/Users/MahdiMoslemi/Desktop/hydor-file/new/FOND_S1.t3s'

    #with open('parameters.txt', 'r') as f:
     #   for x, line in enumerate(f):
      #      if x == 4:
       #         new_points = line
        #        new_points = new_points.replace("\n","")


    #with open(all_points,'w')as f2:
        #f2.write("x y z")
        #f2.write("\n")


    with open(all_points,'w') as f3:
        with open (GEO_t3s,"r") as f:
            for x, line in enumerate(f):
                if "EndHeader" in line:
                    num1 = x

        with open(GEO_t3s, 'r') as f:
            for x, line in enumerate(f):
                if "NodeCount" in line:
                    num2 = x
        with open(GEO_t3s, 'r') as f:
            for x, line in enumerate(f):
                if x == num2:  # we want to find when the connectivities start and when they are finished
                    total_nodes = float(line.split()[1])  # THIS IS THE TOTAL NUMBER OF NODES


                    # READ ALL COORDINATES X, Y and the solution variable (eta or H)
        with open(GEO_t3s, "r") as f:
            for x, line in enumerate(f):
                if num1 < x <= (total_nodes + num1):
                    f3.write(line)

        with open(new_points,'r') as f:
            filedata=f.read()

            filedata =filedata.replace("(","")
            filedata= filedata.replace(")", "")
            filedata= filedata.replace(",", "")
            f3.write(filedata)

sum_points("all_points_v3","/Users/MahdiMoslemi/Desktop/hydor-file/new/FOND_S1.t3s")


def new_mesh_properties(river,edge_file,final_connectivity):
    from scipy.spatial import Delaunay, delaunay_plot_2d
    import csv

    #river = "directory of nodes plus new points"
    #edge_file = " this is the .i2s file related to the wall (first wall nodes)"
    #connectivity = "new connectivities of the simulation with Delaunay"
    #river = "all_points"


    vertices = []
    with open(river, 'r') as f:
        csv1 = csv.reader(f, delimiter=" ")
        for x, row in enumerate(csv1):
                vertices.append([float(row[0]),float(row[1])])
        points = f.readlines()
    print(vertices)

    tri = Delaunay(vertices)

#plt.figure(figsize=(14, 7))
#ax = plt.subplot(111, aspect='equal')
#delaunay_plot_2d(tri, ax=ax)
#plt.show()


    new_connectivity =tri.vertices                   # Here we have all the connectivities which made by delaunay function
    print(new_connectivity)
    with open("connectivity","w") as f:
        for item in new_connectivity:
            f.write(" ".join(map(str, item)))
            f.write("\n")


    with open(edge_file, 'r') as f:
        for x, line in enumerate(f):
            if "EndHeader" in line:
                num = x


    my_line = []
    list_wall= []
    N_lines = 0
    with open(edge_file, 'r') as f:
        for x,line in enumerate(f):
            N_lines += 1
    with open(edge_file, 'r') as f:
        csv1 = csv.reader(f, delimiter=" ")
        for x,line in enumerate(csv1):
            if num+1 < x < N_lines:
         #for x in range(num+1 , 30000,1):
           #print(line)
                l = list(line)
                for i in range(0, len(l), 2):                     #****** in ghesmat moheme ****
                    my_list=str(l[i] +" "+ l[i + 1])
                    #print(my_list)

                 #with open('wall.txt', 'w') as f3:
                    with open(river, 'r') as f2:
                        for y, row in enumerate(f2):
                            if my_list in row:
                                                    # here we have the "points number" of the edge_nodes
                                list_wall = list_wall + [y]

    #print(list_wall)
    with open("red_connect" , "w") as f2:                                       #here I defind the connectivities which are made with 3 points of the edge_nodes
        with open("connectivity", 'r') as f:
            for x, line in enumerate(f):
                if (set(list(map(int,line.split()))).issubset(list_wall)):
                    #print(line)
                    f2.write(line)


    with open("connectivity","r") as f2:         # this is all of the connectivities
        filedata2 = f2.read()

    with open("red_connect" , "r") as f:                #here we have all the connectivities - wall connectivities
        for x,line in enumerate(f):
            filedata1 = line
            filedata2 = filedata2.replace(filedata1, "")

    with open(final_connectivity, "w") as f:
        f.write(filedata2)

new_mesh_properties("all_points_v3","/Users/MahdiMoslemi/Desktop/hydor-file/BND_EASTM.i2s","connectivity_v3")

def connect_plus_1(final_connect,final_connectivity_plus1):
    import pandas as pd

    df = pd.read_csv(final_connect, delimiter=' ', names=['x','y','z'])

    df.x = df.x +1
    df.y = df.y +1
    df.z = df.z +1

    df.to_csv(final_connectivity_plus1, sep=' ', index=False, header=False)

connect_plus_1("connectivity_v3","final_connectivity_plus_1_v3")

N_count = 0
with open("all_points_v3","r") as f:
    for x,line in enumerate(f):
        N_count+= 1
print(N_count)

N_element=0
with open("final_connectivity_plus_1_v3","r") as f:
    for x,line in enumerate(f):
        N_element+= 1
print(N_element)

with open("new_mesh_t3s_v3.t3s","w") as f1:
    with open('/Users/MahdiMoslemi/Desktop/hydor-file/new/FOND_S1.t3s',"r") as f2:

        for x,line in enumerate(f2):
            if 0<=x<=21:
                if "NodeCount" in line:
                    line = line.replace(line.split()[1],str(N_count))
                if "ElementCount" in line:
                    line = line.replace(line.split()[1],str(N_element))
                f1.write(line)

    with open("all_points_v3","r") as f3:
        for x,line in enumerate(f3):
            f1.write(line)

    with open("final_connectivity_plus_1_v3","r") as f4:
        for x,line in enumerate(f4):
            f1.write(line)





