with open("water_depth_2RFM_nodes.xyz","r") as f:
    bp = f.read()

with open("water_depth2_with_interpolate_water_depth1_nodes.xyz","r") as f2:
    for x ,line in enumerate(f2):
        if "\n\n" in line :
            line= line.replace("\n\n","\n")