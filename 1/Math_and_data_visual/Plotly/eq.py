from pathlib import Path
import json
import plotly.express as px
import pandas as pd
path=Path("eq_date\eq_data_30_day_m1.json")
try:
    contents=path.read_text()
except:
    contents=path.read_text(encoding='utf-8')
all_eq_date=json.loads(contents)

path=Path("eq_date/readable_eq_data_1_day.json")
readable_contents=json.dumps(all_eq_date,indent=4)
path.write_text(readable_contents)

all_eq_dicts=all_eq_date['features']
print(len(all_eq_dicts))
mags,titles,lons,lats=[],[],[],[]
for eq_dicts in all_eq_dicts:
    mag=eq_dicts['properties']['mag']
    title=eq_dicts['properties']['title']
    lon=eq_dicts['geometry']['coordinates'][0]
    lat=eq_dicts['geometry']['coordinates'][1]
    titles.append(title)
    lons.append(lon)
    lats.append(lat)
    mags.append(mag)
data=pd.DataFrame(
    data=zip(lons,lats,titles,mags),columns=['经度','纬度','位置','震级']
)
data.head()
fig=px.scatter(
    data,
    x='经度',
    y='纬度',
    range_x=[-200,200],
    range_y=[-90,90],
    width=800,
    height=800,
    title='全球地震散点图',
    size='震级',
    size_max=100,
color='震级',
hover_name='位置'
)
fig.write_html('global_earthquakes,html')
#fig.show()
print(data)