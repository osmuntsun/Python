import geopandas as gpd
import matplotlib.pyplot as plt
import numpy as np

'''
light = gpd.read_file(
    './day-3-Light.csv',
    encoding='utf-8'
    )

# print( light.groupby('district').size() )
'''
village = gpd.read_file(
    './Village_data/Village.shp',
    encoding='utf-8'
    )
village.crs={'init':'epsg:3826'}
# print( village.head(3) )


lib = gpd.read_file(
    './day-3-output/Light.shp',
    encoding='utf-8'
)
lib.crs={'init':'epsg:4326'}
lib=lib.to_crs(epsg=3826)
# print( lib.head(3) )

base = village[village["ADMIT"]=='板橋區'].plot(color='yellow')
lib[lib['address'].str.contains('板橋區')].plot(ax=base)
# plt.show()

result = gpd.tools.sjoin(
    lib,
    village[['ADMIV','ADMIT','geometry']],
    how='left'
    )
# print(result )

group = result.groupby(['ADMIT','ADMIV'])
# print( group.size().reset_index(name='counts') )
# result.plot('ADMIT')
# plt.show()

# intersects 找交集 iterrows 返回元組
counts=[np.sum(row['geometry'].intersects(lib.unary_union)) for idx, row in village.iterrows()]
village['count']=counts
aggre_v=village[['ADMIV','ADMIT','count','geometry']]
# print( aggre_v[aggre_v['count']>0] )

# aggre_v.plot('count')
# plt.show()


# dissolve
# 試著再把資料做一次聚合，使用行政區上色，
# 會用到dissolve，其中第一個參數是要dissolve的欄位，
# aggfunc則是欄位中被合併的資料呈現的方式，
# 我們這邊的聚合方式當然是sum
dis = aggre_v.dissolve('ADMIT',aggfunc='sum')
dis.plot('count')
plt.show()

