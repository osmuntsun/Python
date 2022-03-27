import folium
from folium.plugins import TimeSliderChoropleth
import matplotlib.pyplot as plt
import geopandas as gpd
import pandas as pd
import numpy as np

'''
m = folium.Map((25.0795172,121.485296),zoom_start=19)
folium.CircleMarker(
    location=[25.0795172,121.485296],
    radius=20,
    popup='我家',
    color='#3186cc',
    fill=True,
    fill_color='#3186cc'
).add_to(m)

'''

village=gpd.read_file('./Village_data/Village.shp',encoding='utf-8')
village=village[village.is_valid]
village=village[village['ADMIT']=='永和區']
village.crs = {'init' :'epsg:3826'} # 避免資料沒設，這邊再重新給一次
village=village.to_crs(epsg=4326)
village=village.reset_index()

# m = folium.Map((25.0133904,121.52245),zoom_start=14)
# folium.GeoJson(
#     village.to_json(),
#     name='geojson'
# ).add_to(m)
# folium.LayerControl().add_to(m)
# m.save('try-1.html')


n_periods = 24
n_sample = 12
assert n_sample < n_periods
dt_index = pd.date_range('2012-1-1', periods = n_periods, freq='M').strftime('%s')
styledata = { }

for item in village.index: 
    df = pd.DataFrame({'color': np.random.normal(size=n_periods), 
                       'opacity': np.random.normal(size=n_periods)},
                      index = dt_index)
    df = df.cumsum()
    df.sample(n_sample, replace=False).sort_index()
    styledata[item] = df

styledict = {str(country): data.to_dict(orient='index') for 
             country, data in styledata.items()}
# print(styledict)


m = folium.Map((25.0133904,121.52245), tiles="Cartodb Positron",zoom_start=14)
g = TimeSliderChoropleth(
    village.to_json(),
    styledict = styledict,
    
).add_to(m)
m.save('try-1.html')
