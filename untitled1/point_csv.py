import csv
import numpy as np

filename = '/Users/MahdiMoslemi/Desktop/xyz_b'
with open(filename) as csvfile:
    data = [tuple(map(float, row)) for row in csv.reader(csvfile , delimiter=" ")]
points = np.array(data)

from scipy.spatial import Voronoi, voronoi_plot_2d
vor = Voronoi(points)

import matplotlib.pyplot as plt
plt(vor)
plt.show()

