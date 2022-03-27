# import geopandas as gpd
# from shapely.geometry import Point

# import matplotlib.pyplot as plt
# import pandas as pd
# # gdf_Rail=gpd.read_file('./mapdata202106240917/RAIL_1100406.shp',encoding='utf-8')

# # sample=gdf_Rail.sort_values(by='MDATE')
# # sample.plot(column='RAILNAME') # 顏色
# # plt.show()

# df = pd.read_csv('./Light.csv',encoding='utf-8')
# print(df)

# geom = [Point(xy) for xy in zip(df.TWD97X,df.TWD97Y)]

import numpy as np

# Define vertices of polygon (lat/lon)
v0 = [7.5, -2.5] 
v1 = [2, 3.5]
v2 = [-2, 4]
v3 = [-5.5, -4]
v4 = [0, -10]
lats_vect = np.array([v0[0],v1[0],v2[0],v3[0],v4[0]])
lons_vect = np.array([v0[1],v1[1],v2[1],v3[1],v4[1]])

# Point of interest P
x, y = -6, 5 # x = Lat, y = Lon

