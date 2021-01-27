import os
import pandas as pd

path = os.getcwd()
excel_locations = pd.read_excel(path + "\crawling_Corona.xlsx", engine='openpyxl')

location_count = pd.DataFrame(excel_locations['place'].value_counts())
location_count.to_excel(path+"\location_count.xlsx", engine='openpyxl')
locations = list(location_count.index)


import requests

searching = 'Seoul'
url = 'https://dapi.kakao.com/v2/local/search/keyword.json?query={}'.format(searching)

headers = {
    "Authorization": "KakaoAK bb6e090a8450c62cd93501d68c1b20ef"
    # must put a space after "KakaoAK"
}

places = requests.get(url, headers = headers).json()

def find_places(searching):

    url = 'https://dapi.kakao.com/v2/local/search/keyword.json?query={}'.format(searching)

    headers = {
    "Authorization": "KakaoAK bb6e090a8450c62cd93501d68c1b20ef"
    }

    location = requests.get(url, headers = headers).json()['documents']

    location = location[0]
    name = location['place_name']
    x=location['x']
    y=location['y']
    data = [name, x, y, searching]

    return data

import time
locations_inform = []
count = 0
for location in locations:
    try:
        count = count + 1
        data = find_places(location)
        locations_inform.append(data)
        print(count)
        time.sleep(0.5)
    except:
        pass

locations_inform_df = pd.DataFrame(locations_inform)
locations_inform_df.columns = ['장소','경도','위도','인스타위치명']
locations_inform_df.to_excel(path + '/locations.xlsx', index=False, engine='openpyxl')

