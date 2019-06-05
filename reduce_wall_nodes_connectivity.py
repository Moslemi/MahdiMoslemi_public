edge_file = "/Users/MahdiMoslemi/Desktop/hydor-file/new_outline.i2s"
#edge_file = "/Users/MahdiMoslemi/Desktop/hydor-file/BND_EASTM.i2s"
collected_nodes = "/Users/MahdiMoslemi/Desktop/xyz_b_inside.csv"
connectivity = "/Users/MahdiMoslemi/Desktop/PycharmProjects/mesh_inside_polygone/connectivities"
import csv



with open(edge_file, 'r') as f:
    for x, line in enumerate(f):
        if "EndHeader" in line:
            num = x

my_line = []
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
                 print(my_list)

                 with open('wall.txt', 'w') as f3:
                     with open(collected_nodes, 'r') as f2:
                         for y, row in enumerate(f2):
                             if my_list in row:
                                 # if item in row:
                                 #numb = y + 1
                                #print(numb)
                                 list_wall = list_wall + [y]
                                 #f3.write(str(y+1))
print(list_wall)


#with open(collected_nodes,"r") as f:
 #   for x, line in enumerate(f):
  #      for item in list_wall:
    #        if x==item:
   #             print (line)

counter =1
with open(connectivity,'r') as f:
    for x, line in enumerate(f):
        counter +=1

with open("red_connect" , "w") as f2:
    with open(connectivity, 'r') as f:
        for x , line in enumerate(f):
            if (set(list(map(int, line.split()))).issubset(list_wall)):
                print(line)
                f2.write(line)

#with open("red_connect" , "r") as f:
 #   filedata1 = f.read()
#print(filedata1)
with open(connectivity,"r") as f2:
    filedata2 = f2.read()

with open("red_connect" , "r") as f:
    for x ,line in enumerate(f):
        filedata1 = line
        filedata2 = filedata2.replace(filedata1, "")

with open ("final_url_connect" , "w") as f:
    f.write(filedata2)

#########################################
#from this part we should rebuild the mesh
counter1 =1
with open("final_url_connect",'r') as f4:
    csv5 = csv.reader(f4, delimiter=" ")
    for x, line in enumerate(f4):
        counter1 +=1

counter2 =1
with open(collected_nodes,'r') as f:
    csv4 = csv.reader(f, delimiter =" ")
    for x, line in enumerate(f):
        counter2 +=1

#import operator
#with open('final_url_connect', 'r') as sample:
 #   csv1 = csv.reader(sample, delimiter=" ")
  #  sort = sorted(csv1, key=lambda row: (row[0],row[1]))

#with open('final_url_connect', 'w') as f:
 #   f.write(str(sort))

#with open('final_url_connect', 'r') as f:
 #   fdata = f.read()
#fdata =fdata.replace(" [" , "")
#fdata = fdata.replace("],","\n")
#fdata = fdata.replace("'" , "")
#fdata = fdata.replace("," , "")
#fdata = fdata.replace("[[" , "")
#fdata = fdata.replace("]]" , "")
#with open('final_url_connect', 'w') as f:
#    f.write(fdata)
#from meshpy.tet import MeshInfo, build
#points=[]
#mesh_info = MeshInfo()



#with open (collected_nodes, "r") as f:
   # csv4 = csv.reader(f , delimiter = " ")
  #  for x , row in enumerate(csv4):
 #       points.append((float(row[0]), float(row[1])))
#print(points)
#mesh_info.set_points(points)

#connec = []
#with open (connectivity, "r") as f:
 #   csv4 = csv.reader(f , delimiter = " ")
#    for x , row in enumerate(csv4):
#        connec.append([int(row[0]),int(row[1]),int(row[2])])

#print(connec)
#mesh_info.set_facets(connec)




#mesh = build(mesh_info)
#mesh.write_vtk("test.vtk")