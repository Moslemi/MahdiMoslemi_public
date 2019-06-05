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
            if x>=0:
                vertices.append([float(row[0]),float(row[1])])
                #points = f.readlines()
#print(vertices)

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

new_mesh_properties("all_points_v1","/Users/MahdiMoslemi/Desktop/hydor-file/BND_EASTM.i2s","connectivity_v1")