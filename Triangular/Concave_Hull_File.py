from numpy import array
import os.path
import time

def read_poly(file_name):
    """
    Simple poly-file reader, that creates a python dictionary
    with information about vertices, edges and holes.
    It assumes that vertices have no attributes or boundary markers.
    It assumes that edges have no boundary markers.
    No regional attributes or area constraints are parsed.
    """

    output = {'vertices': None, 'holes': None, 'segments': None}

    # open file and store lines in a list
    file = open(file_name, 'r')
    lines = file.readlines()
    file.close()

    lines = [x.strip('\n').split() for x in lines]

    # Store vertices
    vertices = []
    N_vertices, dimension, attr, bdry_markers = [int(x) for x in lines[0]]
    # We assume attr = bdrt_markers = 0
    for k in range(N_vertices):
        label, x, y = [items for items in lines[k + 1]]
        vertices.append([float(x), float(y)])
    output['vertices'] = array(vertices)

    # Store segments
    segments = []
    N_segments, bdry_markers = [int(x) for x in lines[N_vertices + 1]]
    for k in range(N_segments):
        label, pointer_1, pointer_2 = [items for items in lines[N_vertices + k + 2]]
        segments.append([int(pointer_1) - 1, int(pointer_2) - 1])
    output['segments'] = array(segments)

    # Store holes
    N_holes = int(lines[N_segments + N_vertices + 2][0])
    holes = []
    for k in range(N_holes):
        label, x, y = [items for items in lines[N_segments + N_vertices + 3 + k]]
        holes.append([float(x), float(y)])

    output['holes'] = array(holes)

    return output

import numpy as np
from scipy.spatial import ConvexHull
import matplotlib.pyplot as plt

lake_superior = read_poly("superior.poly")
vertices_ls = lake_superior['vertices']
hull = ConvexHull(vertices_ls)
plt.figure(figsize=(14, 14))
plt.xlim(vertices_ls[:,0].min()-0.01, vertices_ls[:,0].max()+0.01)
plt.ylim(vertices_ls[:,1].min()-0.01, vertices_ls[:,1].max()+0.01)
plt.axis('off')
plt.axes().set_aspect('equal')
plt.plot(vertices_ls[:,0], vertices_ls[:,1], 'b.')
for simplex in hull.simplices:
    plt.plot(vertices_ls[simplex, 0], vertices_ls[simplex, 1], 'r-')

plt.show()

############################

from scipy.spatial import Voronoi, voronoi_plot_2d
vor = Voronoi(vertices_ls)
plt.figure(figsize=(8, 8))
ax = plt.subplot(111, aspect='equal')
voronoi_plot_2d(vor, ax=ax)
plt.xlim( 0.45,  0.50)
plt.ylim(-0.40, -0.35)
plt.show()
#############################

from scipy.spatial import Delaunay, delaunay_plot_2d
tri = Delaunay(vertices_ls)
plt.figure(figsize=(14, 14))
ax = plt.subplot(111, aspect='equal')
delaunay_plot_2d(tri, ax=ax)
plt.show()
####################################

from triangle import triangulate, plot as tplot
cndt = triangulate(lake_superior, 'p')
plt.figure(figsize=(14, 14))
ax = plt.subplot(111, aspect='equal')
tplot.plot(ax, **cndt)
plt.show()

##########
