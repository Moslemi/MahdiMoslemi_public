#A=[(1,20),(2,3),(4,5)]
#A.append((5,6))
#for n in A:
 #   print(n[1:2])
#lis=[(101, 153), (455, 827), (361, 961)]

#print(lis[1][1])
#with open('points','w')as f2:
 #   with open('new_nodes_15','r') as f:
  ##         filedata=f.read()

    #        filedata =filedata.replace("(","")
     #       filedata= filedata.replace(")", "")
      #      filedata= filedata.replace(",", "")
       #     filedata = filedata.replace("None\n", "")
        #    f2.write(filedata)
#from scipy import interpolate


#xx = [1,2,3]
#yy = [4,5,6]
#zz = [7,8,9]

#f = interpolate.interp2d(xx, yy, zz, kind='linear')
#print(int("123\n"))
#l = 1,2,3
#print(l[0])



            # with open(all_points,'w')as f2:
            # f2.write("x y z")
            # f2.write("\n")

with open("all_points_v7", 'w') as f3:  # All points is the file which we want all of the point written inside it
    with open("all_points_v5", "r") as f:
        for x, line in enumerate(f):
            f3.write(line)

    with open("points_lidar_differentzone1", 'r') as f:
        filedata = f.read()

        filedata = filedata.replace("(", "")
        filedata = filedata.replace(")", "")
        filedata = filedata.replace(",", "")
        f3.write(filedata)






