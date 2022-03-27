import geopandas as gpd
import geoplot as gplt
import geoplot.crs as gcrs
import matplotlib.pyplot as plt
import numpy as np



light = gpd.read_file(
    './day-3-Light-output/Light.shp',
    encoding='utf-8'
    )
light = light[light.is_valid]
light = light[
    light['district']=='永和區'
    ]
light.crs = {'init':'epsg:3826'}
light = light.to_crs(epsg=4326)

light['year']=np.random.randint(0,20,size=light.shape[0])


'''
gplt.pointplot(light, 
projection=gcrs.AlbersEqualArea(), 
hue='year', # hue(顏色)繪圖 
legend=True, 
scheme='fisher_jenks', 
figsize=(16, 8)
)



gplt.pointplot(
    light,
    projection=gcrs.AlbersEqualArea(),
    scale='year', # scale作為視覺變數
    legend=True,
    limits=(0,8),
    figsize=(16,8)
    )


light['size']=np.random.randint(
    low=0,
    high=5,
    size=light.shape[0]
    )
gplt.pointplot(light, 
projection=gcrs.AlbersEqualArea(),
hue='size', 
scale='year', 
legend=True ,
limits=(0, 8), 
figsize=(40, 32)
)

plt.show()
'''


village = gpd.read_file(
    './Village_data/Village.shp',
    encoding='utf-8')
village = village[village.is_valid]
village=village[village['ADMIT']=='永和區']

village.crs = {'init':'epsg:3826'}
village = village.to_crs(epsg=4326)

'''
# 面量圖
gplt.choropleth(
    village,
    hue = 'X',
    projection=gcrs.AlbersEqualArea(),
    legend=True,
    edgecolor='white',
    scheme='EqualInterval',
    figsize=(16,8)
)
'''

result=gpd.tools.sjoin(
    light[['geometry','year']], #'size'
    village[['ADMIV','ADMIT','geometry']], 
    op='within',how="right")
result['count']=1
result=result.dissolve(by='ADMIV', aggfunc='sum')
result['year']=result['year']/result['count']
# result['size']=result['size']/result['count']

'''
# 累積圖
gplt.choropleth(result,
    hue='count', 
    projection=gcrs.AlbersEqualArea(),
    legend=True, 
    edgecolor='white', 
    linewidth=0.5,  
    scheme='EqualInterval',
    figsize=(16, 8))

# 另一個呈現方式
ax =gplt.polyplot(
    village,
    projection=gcrs.AlbersEqualArea(), 
    figsize=(16, 8))
gplt.pointplot(light,ax=ax,projection=gcrs.AlbersEqualArea(),  hue='year', legend=True)
'''

# 熱區圖
ax =gplt.polyplot(result,projection=gcrs.AlbersEqualArea(), figsize=(16, 8))
ax=gplt.kdeplot(light,ax=ax,shade=True,projection=gcrs.AlbersEqualArea(),shade_lowest=False)

plt.show()