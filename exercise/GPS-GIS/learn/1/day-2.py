import geopandas as gpd
import matplotlib.pyplot as plt

gdf_rail = gpd.read_file('./mapdata202106240917/RAIL_1100406.shp',encoding='utf-8')
# print(gdf_rail)

# 拿 RAILNAME 欄
subset = gdf_rail['RAILNAME']
# print(subset)

# 拿 列(ROW) 前3列[:3]
subset = gdf_rail.iloc[:3]
# print(subset) 

# 排序 照 MDATE 排序
sample=gdf_rail.sort_values(by='MDATE')
# print(sample)

sample.plot(column='RAILNAME')
plt.show()

