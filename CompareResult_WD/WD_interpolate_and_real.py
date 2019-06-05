

import pandas as pd

df = pd.read_csv("water_depth2_with_interpolate_water_depth1_nodes.xyz", delimiter = ' ', names = ['x','y','z'])
count = len(df.x.index)
#print(df.z)
df2 = pd.read_csv("water_depth_2RFM_nodes.xyz", delimiter = ' ', names = ['x1','y1','z1'])
#print(df2.z1)
df2.z1 = df2.z1-df.z




#print(df_dif)
#df.x.to_csv('error', sep = ' ' , index = False , header = False)
#df.y.to_csv('error', sep = ' ' , index = False , header = False)
df2.to_csv('error.xyz', sep = ' ' , index = False , header = False)
#print(min(df2.z1))
#print(max(df2.z1))