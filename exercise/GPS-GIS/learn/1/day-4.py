import geopandas as gpd
import matplotlib.pyplot as plt

'''
gdf_lib = gpd.read_file(
"./day-3-Library-output/Library.shp",encoding='utf-8'
)

gdf_lib.crs = {'init':'epsg:4326'} # 避免資料沒設，這邊再重新給一次

gdf_lib=gdf_lib.to_crs(epsg=3826)
print( gdf_lib.head(1))

baes = gdf_lib.head(1).buffer(100).plot()
gdf_lib.head(1).plot(ax=baes, marker='o',color='red',markersize=30)
plt.show()

# area是GeoDataFrame中，提供每一筆幾何資料的面積
# resolution参数就用于决定每个四分之一圆弧上使用
# 多少段连续的线段来近似拼接以表示圆的形状，
# 默认参数值为16，足以近似模拟圆面积的99.8%
buffer = gdf_lib.head(1).buffer(100,resolution=20)
area = buffer.area
print(f'得出:{area[0]:.3f}')

#envelope是整個GeoDataFrame中，
# 每一筆資料包覆的長方形範圍，它是一個四角坐標
envelope=buffer.envelope
print(envelope)

# convex hull與envelope類似但不一樣，
# 它是包住每一個資料的凸殼多邊形
convexhull=buffer.convex_hull
print(convexhull)

# 我們連同原本的形狀一起套疊(原本的形狀是由點buffer成面)
base=envelope.plot()
convexhull.plot(ax=base,color='brown')
gdf_lib.head(1).plot(ax=base,  color='red')
plt.show()

base=buffer.scale(10,5).plot(color='yellow')
buffer.plot(ax=base,color='brown')
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
base = p1.plot(color='red')
p2.plot(ax=base, color='yellow')
plt.show()

# 第一個運算子是intersection，算出的是兩個圖形的交集，
# 我們分別使用不同的顏色給p1與p2，並把交集的部分給定黃色
intersection = gpd.overlay(p1,p2,  how='intersection')
base=p1.plot(color='blue')
p2.plot(ax=base,color='brown')
intersection.plot(ax=base,color='yellow')
plt.show()

# 第二個是union聯集，
# 一樣給予上色，黃色的部分，就是聯集的部分
union = gpd.overlay(p1,p2,how='union')
base=p1.plot(color='blue')
p2.plot(ax=base, color='brown')
union.plot(ax=base,color='yellow')
plt.show()

# difference會算出兩個幾何的差異，一樣以黃色表示
difference= gpd.overlay(p1,p2,how='difference')
base = p1.plot(color='blue')
p2.plot(ax=base, color='brown')
difference.plot(ax=base,color='yellow')
plt.show()