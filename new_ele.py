import numpy as np
from planar import Polygon
import csv

vertices = '/Users/MahdiMoslemi/Desktop/PycharmProjects/mesh_inside_polygone/SURFACE LIBRE_S1.t3s'
connectivities = '/Users/MahdiMoslemi/Desktop/PycharmProjects/mesh_inside_polygone/final_url_connect'
topology = '/Users/MahdiMoslemi/Desktop/Hydro-Quebec-Proj/LIDAR/20JAN2004/QUADRILLAGE_05_METRES/UTM_17_ORTHOMETRIQUE/33d012000201_utm_17.grd'

lists= []
def elements(a,b,c):
    with open(connectivities,"r") as f:

        for x , line in enumerate(f):
            a== line[0]
            b== line[1]
            c== line[2]

            with open(vertices,"r") as f2:
                for y , row in enumerate(f2):
                    if y== a:
                        lists.append(float(row[0]),float(row[1]))
                    if y== b:
                        lists.append(float(row[0]), float(row[1]))
                    if y== c:
                        lists.append(float(row[0]), float(row[1]))
                        print(lists)
elements(10,1,8)
print(lists)