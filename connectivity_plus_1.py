def connect_plus_1(final_connect):
    import pandas as pd

    df = pd.read_csv(final_connect, delimiter=' ', names=['x','y','z'])

    df.x = df.x +1
    df.y = df.y +1
    df.z = df.z +1

    df.to_csv("final_connect_plus_1_v2", sep=' ', index=False, header=False)

connect_plus_1("connectivity_v1")