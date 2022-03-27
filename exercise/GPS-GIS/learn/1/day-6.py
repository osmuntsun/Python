import geopandas as gpd
import geohash
from shapely.geometry import Polygon
import matplotlib.pyplot as plt

light = gpd.read_file(
    './day-3-Light-output/Light.shp',
    encoding='utf-8'
    )

light = light[light.is_valid]

light=light[light['district']=='永和區']
# print(light)
light.crs={'init':'epsg:3826'}
light = light.to_crs(epsg=4326)
# print(light)

light['geohash']=[geohash.encode(row['geometry'].y,row['geometry'].x, precision=7) for idx,row in light.iterrows()]
# print(light)

group=light.groupby('geohash')
group=group.size().reset_index(name='counts')
# print(group)

geohashs=[]

for idx,row in group.iterrows():
    decoded = geohash.bbox(row['geohash'])
    geohashs.append(
        Polygon([(decoded['s'], decoded['w']),
         (decoded['s'],decoded['e']),
          (decoded['n'], decoded['e']),
           (decoded['n'],decoded['w'])])
           )

g = gpd.GeoSeries(geohashs)        
g_aggr = gpd.GeoDataFrame(group)
g_aggr['geometry']=g
g_aggr.plot('counts')
plt.show()