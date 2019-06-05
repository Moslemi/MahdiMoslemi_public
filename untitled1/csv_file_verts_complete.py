import csv
import os

filename = 'circle.csv'
directory = '/home/zeffii/Desktop'  # <-- if you have linux or osx
# directory = r'c:\some\directory'  # <-- if windows, the r is important
# directory = 'c:/some/directory'  # <-- if windows (alternative)

fullpath = os.path.join(directory, filename)

with open(fullpath, 'r', newline='') as csvfile:
    ofile = csv.reader(csvfile, delimiter=',')
    next(ofile) # <-- skip the x,y,z header

    # this makes a generator of the remaining non-empty lines
    rows = (r for r in ofile if r)

    # this converts the string representation of each line
    # to an x,y,z list, and stores it in the verts list.
    verts = [[float(i) for i in r[:2]] for r in rows]

if verts:
    # curve coordinates require a 4th 'W'(weight) component,
    # the +[0.0] adds that for us
    out2 = []
    [out2.extend(list(i)+[0.0]) for i in verts]

    # has one coordinate by default, we add one fewer than we need
    num_points_to_add = len(verts) - 1
    curve = bpy.data.curves.new("path_name", type='CURVE')
    polyline = curve.splines.new(type='POLY')
    polyline.points.add(num_points_to_add)
    polyline.points.foreach_set('co', out2)

    obj = bpy.data.objects.new("obj_name", curve)
    scene = bpy.context.scene
    scene.objects.link(obj)