import requests
import os
import pandas as pd
import json

service_name = "StatisticSearch"
api_key = "BI5X80RRY4XIAS7FQ4BH"
file_type = "json"
lang_type = "kr"
start_no = "1"
end_no = "400"
stat_code = "064Y001"
cycle_type = "DD"
start_date = "20200401"
end_date = "20210315"
item_no1 = "0001000"

url = "/".join(["http://ecos.bok.or.kr/api",service_name,
             api_key, file_type, lang_type, start_no, end_no,
             stat_code, cycle_type, start_date, end_date, item_no1])

print(url)

try:
    response = requests.get(url)
    if response.status_code == 200:
        data = response.text
    else:
        print("에러")
except Exception as e:
    print(e)

j_data = json.loads(data)
body = j_data['StatisticSearch']['row']
kospi_data = pd.json_normalize(body)

path = os.getcwd()
kospi_data.to_excel(path + "/data/kospi20200401_20210216.xlsx", engine='openpyxl')
