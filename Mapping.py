import os
import pandas as pd

path = os.getcwd()

location_counts_df = pd.read_excel(path+'/location_count.xlsx', index_col = 0, engine='openpyxl')
location_df = pd.read_excel(path+'/locations.xlsx', engine='openpyxl')

location_data = pd.merge(location_df, location_counts_df,
                         how = 'inner', left_on = '인스타위치명', right_index=True)

location_data.to_excel(path+"\location_data.xlsx", engine='openpyxl')


import folium
from folium.plugins import MarkerCluster

Seoul_Station = [37.553664, 126.9669926]  # folium 기준점 변수
map_Seoul = folium.Map(location=Seoul_Station, zoom_start=11)  # folium 장소, 확대 특정

locations = []
names = []

for i in range(len(location_data)):
    data = location_data.iloc[i]  # 행 하나씩
    locations.append((float(data['위도']),float(data['경도'])))    # 위도 , 경도 순으로..
    names.append(data['장소'])


marker_cluster = MarkerCluster(
    locations=locations, popups=names, #popup이름
    name='(#)Corona Posing Place',
    overlay=False, #layer 겹치기
    control=True,
)
marker_cluster.add_to(map_Seoul)



for i in range(len(location_data)):
    name = location_data ['장소'][i]    # 공식명칭
    size = int(location_data ['place count'][i]) * 3        # 게시글 개수
    long = float(location_data['위도'][i])
    lat = float(location_data['경도'][i])
    folium.CircleMarker((long,lat), radius = size, color='blue', popup=name, control=False).add_to(map_Seoul)

import webbrowser

map_Seoul.save(path + "\#Corona Posting Places.html")
url = path + "\#Corona Posting Places.html"
webbrowser.open(url)