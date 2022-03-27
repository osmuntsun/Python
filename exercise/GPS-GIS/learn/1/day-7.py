import geopandas as gpd
from shapely.geometry import LineString,Point
import matplotlib.pyplot as plt

'''
line1 = LineString([(0, 0), (50, 50), (100, 100)]) 
line2 = LineString([(10, 0), (60, 50), (110, 100)]) 
lines = gpd.GeoDataFrame()
lines['geometry'] = [line1,line2]
lines.plot()

base=lines.plot()
points = gpd.GeoDataFrame()
intpoints=[row['geometry'].interpolate(50) for idx,row in lines.iterrows()]
intpoints+=[row['geometry'].interpolate(25) for idx,row in lines.iterrows()]
intpoints+=[row['geometry'].interpolate(75) for idx,row in lines.iterrows()]
points['geometry'] = intpoints
points.plot(ax=base)
plt.show()
'''

'''
LineString([(0, 0), (50, 50), (100, 100)]).project(Point(50,0))
lines = gpd.GeoDataFrame()
lines['geometry'] = [LineString([(0, 0), (50, 50), (100, 100)])]
base=lines.plot()

points = gpd.GeoDataFrame()
points['geometry'] = [Point(50,0)]
points.plot(ax=base)
plt.show()


lines = gpd.GeoDataFrame()
lines['geometry'] = [LineString([(0, 0), (50, 50), (100, 100)])]
base=lines.plot()

points = gpd.GeoDataFrame()
points['geometry'] = [Point(50,50)]
points.plot(ax=base)
LineString([(0, 0), (50, 50), (100, 100)]).project(Point(50,50))
plt.show()
'''


p1=gpd.read_file('./day-3-Library-output/Library.shp',encoding='utf-8').head(1)
p1.crs = {'init' :'epsg:4326'} # 避免資料沒設，這邊再重新給一次
p1=p1.to_crs(epsg=3826)
p1['geometry']=p1.buffer(30).translate(xoff=20.0, yoff=0.0)

p2=gpd.read_file('./day-3-Library-output/Library.shp',encoding='utf-8').head(1)
p2.crs = {'init' :'epsg:4326'} # 避免資料沒設，這邊再重新給一次
p2=p2.to_crs(epsg=3826)
p2['geometry']=p2.buffer(30)
base=p1.plot(color='blue')
p2.plot(ax=base,color='brown')
plt.show()

print(f"de-9im輸出值：{p1.at[0,'geometry'].relate(p2.at[0,'geometry'])}" )