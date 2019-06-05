import pandas as pd

df = pd.read_csv('/Users/MahdiMoslemi/Desktop/PycharmProjects/mesh_inside_polygone/def_element/final_url_connect', delimiter = ' ', names = ['x','y','z'])
count = len(df.x.index)
df.x = df.x +1
df.y = df.y +1
df.z = df.z +1

print(df)
df.to_csv('final_url_plus_1_new', sep = ' ' , index = False , header = False)