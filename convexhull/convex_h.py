from scipy.spatial import ConvexHull
from numpy import array
import csv
import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection
import numpy as np

lake_superior = "/Users/MahdiMoslemi/Desktop/xyz_b_inside.csv"

points = []
with open(lake_superior, 'r') as f:
    csv1 = csv.reader(f, delimiter=" ")
    for x , row in enumerate(csv1):
        points.append([float(row[0]),float(row[1])])
    #print(vertices)
hull = ConvexHull(points)
indices = hull.simplices
vertices = points[indices]