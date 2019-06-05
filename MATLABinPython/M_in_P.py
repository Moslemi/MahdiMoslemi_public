from shapely.geometry import Point
from shapely.geometry.polygon import Polygon
from numpy import array


url_node_mesh= '/Users/MahdiMoslemi/Desktop/hydor-file/FOND.t3s'
with open(url_node_mesh, 'r') as f1:
    for x, line in enumerate(f1):
        if "NodeCount" in line:
            num1 = x

with open(url_node_mesh, 'r') as f:
    for x, line in enumerate(f):
        if x == num1:
            num2 = float(line.split()[1])

with open(url_node_mesh, 'r') as f1:
    for x, line in enumerate(f1):
        if "EndHeader" in line:
            num3 = x

with open('nodes_New_mesh', 'w') as f:
    with open(url_node_mesh, 'r') as f1:
        for i, line in enumerate(f1):
            if num3 < i <= num2 + num3:
                f.write(line)





# getting nodes from csv file
with open('/Users/MahdiMoslemi/Desktop/xyz_b_inside', 'w') as f1:
    with open('nodes_New_mesh', 'r') as f:

        for x , line in enumerate(f):
            pointX = float(line.split()[0])
            pointY = float(line.split()[1])
            pointZ = float(line.split()[2])             # take the 1th and 2th columns from the row
            coordList=Point([pointX, pointY])
            polygon = Polygon([(680754.765907,5793071.325022),
                               (682888.213858,5793582.647258),
                               (684874.730132,5794540.641793),
                               (687396.077710,5794928.541420),
                               (688336.440443,5795146.000302),
                               (690416.992990,5796732.862414),
                               (690875.419823,5799777.286763),
                               (689841.020816,5800100.536453),
                               (689682.334605,5799042.628378),
                               (689341.453114,5798613.587881),
                               (689270.925909,5797602.697943),
                               (687948.540816,5796938.566762),
                               (684786.571125,5796256.803781),
                               (679996.598453,5794758.100675),
                               (680754.765907,5793071.325022)])
            if (polygon.contains(coordList)) is False:
                f1.write('%.6f' % pointX)
                f1.write(' %.6f' % pointY)
                f1.write(' %.6f' % pointZ)
                f1.write("\n")

#######
url_main_nodes='/Users/MahdiMoslemi/Desktop/xyz_b_inside'
url_additional_nodes='/Users/MahdiMoslemi/Desktop/hydor-file/New Mesh.t3s'


with open(url_additional_nodes, 'r') as f1:
    for x, line in enumerate(f1):
        if "NodeCount" in line:
            num1 = x

with open(url_additional_nodes, 'r') as f:
    for x, line in enumerate(f):
        if x == num1:
            num2 = float(line.split()[1])

with open(url_additional_nodes, 'r') as f1:
    for x, line in enumerate(f1):
        if "EndHeader" in line:
            num3 = x

with open(url_main_nodes, 'a') as f:
    with open(url_additional_nodes, 'r') as f1:
        for i, line in enumerate(f1):
            if num3 < i <= num2 + num3:
                f.write(line)

countline =1
with open (url_main_nodes, 'r') as f:
    for x,line in enumerate(f):
        countline += 1

def read_poly(file_name):
    """
    Simple poly-file reader, that creates a python dictionary
    with information about vertices, edges and holes.
    It assumes that vertices have no attributes or boundary markers.
    It assumes that edges have no boundary markers.
    No regional attributes or area constraints are parsed.
    """

    output = {'vertices': None, 'holes': None}

    # open file and store lines in a list
    file = open(file_name, 'r')
    lines = file.readlines()
    file.close()

    lines = [x.strip('\n').split() for x in lines]

    # Store vertices
    vertices = []
    dimension = [int(x) for x in lines[0]]
    # We assume attr = bdrt_markers = 0
    for k in range(countline):
        label, x, y = [items for items in lines[k + 1]]
        vertices.append([float(x), float(y)])
    output['vertices'] = array(vertices)

    # Store holes
   # N_holes = int(lines[N_segments + N_vertices + 2][0])
    #holes = []
    #for k in range(N_holes):
     #   label, x, y = [items for items in lines[N_segments + N_vertices + 3 + k]]
      #  holes.append([float(x), float(y)])

#    output['holes'] = array(holes)

    return output

from scipy.spatial import Delaunay, delaunay_plot_2d
lake_superior = read_poly(url_main_nodes)
vertices_ls = lake_superior['vertices']
tri = Delaunay(vertices_ls)
plt.figure(figsize=(14, 14))
ax = plt.subplot(111, aspect='equal')
delaunay_plot_2d(tri, ax=ax)
plt.show()