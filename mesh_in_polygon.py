from numpy import array
import csv
import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection
import numpy as np
collected_nodes = "/Users/MahdiMoslemi/Desktop/xyz_b_inside.csv"

edge_file = "/Users/MahdiMoslemi/Desktop/hydor-file/BND_EASTM.i2s"

lake_superior = "/Users/MahdiMoslemi/Desktop/xyz_b_inside.csv"
with open(lake_superior, 'r') as sample:
    csv1 = csv.reader(sample, delimiter=" ")
    sort = sorted(csv1, key=lambda row: (row[0],row[1]))

with open(lake_superior, 'w') as f:
    f.write(str(sort))

with open(lake_superior, 'r') as f:
    fdata = f.read()
fdata =fdata.replace(" [" , "")
fdata = fdata.replace("],","\n")
fdata = fdata.replace("'" , "")
fdata = fdata.replace("," , "")
fdata = fdata.replace("[[" , "")
fdata = fdata.replace("]]" , "")
with open(lake_superior, 'w') as f:
    f.write(fdata)

vertices = []
with open(lake_superior, 'r') as f:
    csv1 = csv.reader(f, delimiter=" ")
    for x , row in enumerate(csv1):
        vertices.append([float(row[0]),float(row[1])])
    points = f.readlines()
    print(vertices)


from scipy.spatial import Delaunay, delaunay_plot_2d
tri = Delaunay(vertices)
plt.figure(figsize=(14, 7))
ax = plt.subplot(111, aspect='equal')
delaunay_plot_2d(tri, ax=ax)
#plt.show()

connectivities=tri.vertices

with open('connectivities','w') as f:
    for item in connectivities:
        #f.write("%s\n" %item)
        f.write(" ".join(map(str, item)))
        f.write("\n")






import math

edges = set()
edge_points = []
alpha = 0.001


points = np.loadtxt(lake_superior, delimiter=" ", usecols=(0, 1))

#

with open(edge_file, 'r') as f:
    for x, line in enumerate(f):
        if "EndHeader" in line:
            num = x
list_wall= []
N_lines = -1
with open(edge_file, 'r') as f:
    for x, line in enumerate(f):
        N_lines += 1
with open(edge_file, 'r') as f:
    csv1 = csv.reader(f, delimiter=" ")
    for x,line in enumerate(csv1):
        if num+1<x< N_lines:
         #for x in range(num+1 , 30000,1):
           #print(line)
             l = list(line)
             for i in range(0, len(l), 2):                     #****** in ghesmat moheme ****
                 my_list=str(l[i] +" "+ l[i + 1])
                 #print(my_list)

                 with open('wall.txt', 'w') as f3:
                     with open(collected_nodes, 'r') as f2:
                         for y, row in enumerate(f2):
                             if my_list in row:
                                 # if item in row:
                                 #numb = y + 1
                                #print(numb)
                                 list_wall = list_wall + [y]



print(tri.vertices)
# loop over triangles:
# ia, ib, ic = indices of corner points of the triangle
for ia, ib, ic in tri.vertices:

    pa = points[ia]
    pb = points[ib]
    pc = points[ic]

    # Lengths of sides of triangle
    a = math.sqrt((pa[0]-pb[0])**2 + (pa[1]-pb[1])**2)
    b = math.sqrt((pb[0]-pc[0])**2 + (pb[1]-pc[1])**2)
    c = math.sqrt((pc[0]-pa[0])**2 + (pc[1]-pa[1])**2)

    # Semiperimeter of triangle
    s = (a + b + c)/2.0

    # Area of triangle by Heron's formula
    area = math.sqrt(s*(s-a)*(s-b)*(s-c))

    circum_r = a*b*c/(4.0*area)


    def add_edge(i, j):
        """Add a line between the i-th and j-th points, if not in the list already"""
        if (i, j) in edges or (j, i) in edges:
            # already added
            return
        edges.add((i, j))
        edge_points.append(points[[i, j]])

    def remove_edge(i,j,k):
        if (i,j) in edge and (j,k) in edge:
            return
        edge = edge.replace((i,j),"")
        edge = edge.replace((j, k), "")
    # Here's the radius filter.
    if circum_r < 1.0/alpha:
        add_edge(ia, ib)
        add_edge(ib, ic)
        add_edge(ic, ia)

#    for i, j, k in list_wall:
 #       remove_edge(i,j,k)
lines = LineCollection(edge_points)
plt.figure()
plt.title('Alpha=1000.0 Delaunay triangulation')
plt.gca().add_collection(lines)
#plt.show()
plt.plot(points[:,0], points[:,1], 'o', hold=1)
plt.show()
#print(points)