# mpi.run.openmpi -np 2 -machine file "directory" python "name of the file"
import csv
from operator import itemgetter
from interpolation import interpol
from cut_elements import check_element
from inside_polygon import inside
import math
import numpy as np
from mpi4py import MPI
comm = MPI.COMM_WORLD

rank = comm.rank
size = comm.size
name = MPI.Get_processor_name()

with open ('parameters.txt','r') as f:
    for x, line in enumerate(f):
        if x == 1:
            topology1 = line[0]
            topology1 = topology1.replace("\n","")

            print(topology1)

            topology2 = line[1]
            topology2 = topology2.replace("\n", "")

            print(topology2)


        if x == 4:
            new_points1 = line[0]
            new_points1 = new_points1.replace("\n", "")

            print(new_points1)

            new_points2 = line[1]
            new_points2 = new_points2.replace("\n", "")

            print(new_points2)


water_depth_difference = '/Users/MahdiMoslemi/Desktop/PycharmProjects/CompareResult_WD/error.t3s'
with open(water_depth_difference, 'r') as f1:
    for x, line in enumerate(f1):  # with enumerate function we make a relationship between 2 parameeters of (x and line). x is the number of the line, and line is the content of each line
        if "EndHeader" in line:
            num1 = x  # x is the number of the line which  coordinate with start

with open(water_depth_difference, 'r') as f1:
    for x, line in enumerate(f1):
        if "NodeCount" in line:
            num2 = x
with open(water_depth_difference, 'r') as f:
    for x, line in enumerate(f):
        if x == num2:  # we want to find when the connectivities start and when they are finished
            total_nodes = float(line.split()[1])  # THIS IS THE TOTAL NUMBER OF NODES


                # READ ALL COORDINATES X, Y and the solution variable (eta or H)
with open('connect', 'w') as f3:
    with open(water_depth_difference, "r") as f2:
        for x, line in enumerate(f2):
            if num1 - 2 < x <= (total_nodes + num1):
                f3.write(line)

with open('connect', "r") as f:
    for x, line in enumerate(f):
        if x >= 0:
            points_new = f.readlines()
print(points_new[1])

    # we want to extract the connectivities of the elements
with open(water_depth_difference, 'r') as f1:
    for x, line in enumerate(f1):
        if "ElementCount" in line:
            num4 = x

with open(water_depth_difference, 'r') as f:
    for x, line in enumerate(f):
        if x == num4:
            total_elements = float(line.split()[1])

    # open the lidar data. Each line of Lidar contains  x y z
#with open(topology, "r") as f3:
 #   lidar = f3.readlines()

with open(water_depth_difference, "r") as f:
    csvfile = csv.reader(f, delimiter=' ')  # Try to read old connectivities



    for x, line in enumerate(csvfile):
        if num1 + total_nodes < x <= num1 + total_nodes + total_elements:
            with open('log_file.txt', 'a') as flog:
                flog.write("processing element=")
                flog.write(str(int(x - total_nodes - num1)))
                flog.write("\n")
                    # a ,b,c are node numbers
            a = line[0]
            b = line[1]
            c = line[2]

                # pa,pb,pc are the nodes represented by x,y, eta or H
            pa = points_new[int(a)]
            pb = points_new[int(b)]
            pc = points_new[int(c)]
            cut_element_new = []
                # first find if the element is wet, dry, or cut elemets
            if max(abs(float(pa.split()[2])),abs(float(pb.split()[2])),abs(float(pc.split()[2]))) > 0.5:
                cut_element_new = str(a+" "+b+" "+c)



                # cut_element contains [(x1,y1),(x2,y2),(x3,y3),(x1,y1)] for defining the polygon
                with open('log_file2.txt', 'a') as flog:
                    #flog.write("cut_element=")
                    flog.write(str(cut_element_new))
                    flog.write("\n")






def ORIGINAL_FUNCTION(lidar,new_points):

    with open ('parameters.txt','r') as f:
        for x, line in enumerate(f):
            if x == 0:
                water_depth = line
                water_depth = water_depth.replace("\n","")

            #if x == 1:
             #   topology = line
              #  topology = topology.replace("\n","")

            if x == 2:
                epsilon = float(line)

            if x == 3:
                alpha = float(line)

            #if x == 4:
             #   new_points = line

      #          print("epsilon",)

    #READ VECTOR SOLUTION (either eta or H)

    with open(water_depth, 'r') as f1:
        for x, line in enumerate(f1):        #with enumerate function we make a relationship between 2 parameeters of (x and line). x is the number of the line, and line is the content of each line
            if "EndHeader" in line:
                num1 = x     # x is the number of the line which  coordinate with start

    with open(water_depth, 'r') as f1:
        for x, line in enumerate(f1):
            if "NodeCount" in line:
                num2 = x
    with open(water_depth, 'r') as f:
        for x, line in enumerate(f):
            if x == num2:                          # we want to find when the connectivities start and when they are finished
                total_nodes = float(line.split()[1])   # THIS IS THE TOTAL NUMBER OF NODES


                # READ ALL COORDINATES X, Y and the solution variable (eta or H)
    with open('coordinate','w') as f3:
        with open(water_depth, "r") as f2:
            for x, line in enumerate(f2):
                if num1-2 < x <= (total_nodes +num1):
                    f3.write(line)

    with open('coordinate', "r") as f:
        for x, line in enumerate(f):
            if x>=0:
                points = f.readlines()
    print(points[1])







    #we want to extract the connectivities of the elements


    with open("log_file2.txt","r") as f:
        csvfile = csv.reader(f, delimiter =' ')  #  Try to read old connectivities

        with open('log_file3.txt','a') as flog:
            flog.write("epsilon=")
            flog.write(str(epsilon))
            flog.write("\n")

            flog.write("alpha=")
            flog.write(str(alpha))
            flog.write("\n")


        total_number_newpoints = 0
        for x, line in enumerate(csvfile):
            if x>=0:
                with open('log_file3.txt', 'a') as flog:
                    flog.write("processing element=")
                    flog.write(str(int(x-total_nodes-num1)))
                    flog.write("\n")
            #a ,b,c are node numbers
                a = line[0]
                b = line[1]
                c = line[2]

    # pa,pb,pc are the nodes represented by x,y, eta or H
                pa = points[int(a)]
                pb = points[int(b)]
                pc = points[int(c)]
                cut_element = []
            # first find if the element is wet, dry, or cut elemets
                cut_element = check_element(pa, pb, pc)

    # cut_element contains [(x1,y1),(x2,y2),(x3,y3),(x1,y1)] for defining the polygon
                with open('log_file3.txt', 'a') as flog:
                    flog.write("cut_element=")
                    flog.write(str(cut_element))
                    flog.write("\n")

                if cut_element != []:
                    #element = Polygon(cut_element)



            #we should do the loop for cut-elements only
            #we want to check all the lidar points to see if they are in the cut element
                    A = []
                    for nodes in lidar:
    # now we reduce the lidar nodes which we want to check for each element to the min(x1,x2,x3) and min(y1,y2,y3) till max(x1,x2,x3) and max(y1,y2,y3)
                        xmin = min(float(pa.split()[0]),float(pb.split()[0]),float(pc.split()[0]))
                        xmax = max(float(pa.split()[0]),float(pb.split()[0]),float(pc.split()[0]))
                        ymin = min(float(pa.split()[1]),float(pb.split()[1]),float(pc.split()[1]))
                        ymax = max(float(pa.split()[1]),float(pb.split()[1]),float(pc.split()[1]))



                        if ((xmin<float(nodes.split()[0])<xmax) and
                                (ymin<float(nodes.split()[1]) < ymax)):
                            #coordList = Point([float(nodes.split()[0]), float(nodes.split()[1])])  # check if the lidar point is inside the rectangal
                            x1 = cut_element[0][0]
                            y1 = cut_element[0][1]
                            x2 = cut_element[1][0]
                            y2 = cut_element[1][1]
                            x3 = cut_element[2][0]
                            y3 = cut_element[2][1]

                            xsi, eta = inside(float(nodes.split()[0]),float(nodes.split()[1]),x1,y1,x2,y2,x3,y3)
                        # here we try to find if the the point is inside the element
                            #if element.contains(coordList) is True:
                            if (0.0 < xsi < 1.0 and 0.0 < eta < 1.0):
                                d1 = math.sqrt(eta**2 + xsi**2)
                                d2 = math.sqrt((eta-1.0)**2 + xsi**2)
                                d3 = math.sqrt((xsi-1.0)**2+(eta**2))
                                if min(d1, d2, d3) > math.sqrt(2)/10.0:                # WE WANT TO AVOID OF COLLECTING POINTS WHICH ARE NEAR THE VERTICES
                                    xnew = float(nodes.split()[0])
                                    ynew = float(nodes.split()[1])
                            # "A" is a list which contains all the lidar points inside th element



                        # We want to interpolate H for the Lidar point located in the element
                                    Hnew = interpol(float(pa.split()[0]),float(pa.split()[1]),float(pa.split()[2]),float(pb.split()[0]),float(pb.split()[1]),float(pb.split()[2]),float(pc.split()[0]),float(pc.split()[1]),float(pc.split()[2]),xnew,ynew)

                                    if Hnew < alpha*epsilon:                           # We changed abs(Hnew) with Hnew
                                        A = A+ [(xnew,ynew,float(nodes.split()[2]))]

                                # done for the current element
                    if A!=[]:
                        with open(new_points, "a") as feta:

                        # we are trying to find the points which are  making bump(max of z) or valley(min of z)
                            feta.write(str(max(A,key=itemgetter(2))))
                            feta.write("\n")
                            total_number_newpoints= total_number_newpoints + 1
                            if max(A,key=itemgetter(2)) != min(A,key=itemgetter(2)):
                                feta.write(str(min(A,key=itemgetter(2))))
                                feta.write("\n")
                                total_number_newpoints = total_number_newpoints + 1
                                with open('log_file3.txt', 'a') as flog:
                                    flog.write("done with this cut_element=")
                                    flog.write(str(cut_element))
                                    flog.write("\n")
                                    cut_element = []

    with open('log_file3.txt', 'a') as flog:
        flog.write("processing element done")
        flog.write("\n")
        flog.write("total number points = ")
        flog.write(str(total_number_newpoints))
        flog.write("\n")

if rank == 1:
        # open the lidar data. Each line of Lidar contains  x y z
    with open(topology1, "r") as f3:
        lidar = f3.readlines()
    ORIGINAL_FUNCTION(lidar,new_points1)
        ### do the function and make the file ###
    with open(new_points1, 'r') as f:
        data = f.read()
    comm.send(data, dest=0)
    print('from rank', rank, 'we sent', data)

elif rank == 2:
            # open the lidar data. Each line of Lidar contains  x y z
    with open(topology2, "r") as f3:
        lidar = f3.readlines()
    ORIGINAL_FUNCTION(lidar, new_points2)
            ### do the function and make the file ###
    with open(new_points2, 'r') as f:
        data = f.read()
    comm.send(data, dest=0)
    print('from rank', rank, 'we sent',data)


else:
    data = None



#sum_points("all_points_v5","/Users/MahdiMoslemi/Desktop/PycharmProjects/mesh_inside_polygone/def_element/v4/FOND_S1-v4.t3s")


if rank == 0:

    with open('new_points3','w') as f3:

        with open(new_points1,'r') as f1:
            for x,line in enumerate(f1):
                f3.write(line)

        with open(new_points2,'r') as f2:
            for x1 , line1 in enumerate(f2):
                f3.write(line1)


