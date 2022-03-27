import pandas as pd
from shapely.geometry import Point
import geopandas as gpd
import matplotlib.pyplot as plt
import requests, json
import os

'''
df = pd.read_csv('./day-3-Light.csv',encoding='utf-8')
# print(df)

geom = [Point(xy) for xy in zip(df.TWD97X,df.TWD97Y)]
# print(geom)

crs = {'init': 'epsg:4326'}
gdf = gpd.GeoDataFrame(df, crs=crs, geometry=geom)
# print(gdf)

gdf[gdf['district']=='永和區'].plot(column='address')
plt.show()

if 'day-3-Light-output' in os.listdir():
    gdf.to_file(
        driver = 'ESRI Shapefile', 
        filename = './day-3-Light-output/Light.shp',
        encoding= 'utf-8'
    )
else:
    os.mkdir('day-3-Light-output')
    gdf.to_file(
        driver = 'ESRI Shapefile', 
        filename = './day-3-Light-output/Light.shp',
        encoding= 'utf-8'
    )    
'''


df = pd.read_csv('./day-3-Library.csv',encoding='utf-8')
# print(df.head().iterrows())

def rest(address):

    url = f'https://api.tomtom.com/search/2/geocode/{address}.json?&key=Hq7IVCKeIQAtpCt14jBGGqCe7ASI34O2&countrySet=TWN&language=zh-TW&limit=1'
    response = requests.get(url)
    data = response.text
    js = json.loads(str(data))
    # 加以下這句
    dic_lat = js['results'][0]['position']['lat']
    dic_lon = js['results'][0]['position']['lon']
    dic_tuple = (dic_lon,dic_lat)
    return dic_tuple


geom = [Point(rest(row.address)) for idx, row in df.head().iterrows()]
# print(geom)

crs = {'init': 'epsg:4326'}
gdf = gpd.GeoDataFrame(df.head(), crs=crs, geometry=geom)
print(gdf)

gdf.plot(column='address')
plt.show()



if 'day-3-Library-output' in os.listdir():
    gdf.to_file(
        driver = 'ESRI Shapefile', 
        filename = './day-3-output/Library.shp',
        encoding= 'utf-8'
    )
else:
    os.mkdir('day-3-Library-output')
    gdf.to_file(
        driver = 'ESRI Shapefile', 
        filename = './day-3-Library-output/Library.shp',
        encoding= 'utf-8'
    )    
