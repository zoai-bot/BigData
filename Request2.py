import requests, bs4
import pandas as pd
import urllib.request
import os

url = 'http://openapi.data.go.kr/openapi/service/rest/Covid19/getCovid19InfStateJson'

service_key = 'bVMV0wcVFsaJZ%2BLA0IACNG4V3D3DjRmRhBeFe1etm4WhpPnz%2FxKgZKfoLobxeleobKFFH%2Fo%2F56jkx%2BenpRpcGA%3D%3D'

params = (
    '?serviceKey=' + service_key +
    '&numOfRows=20' +
    '&pageNo=1'+
    '&startCreateDt=20200401'+
    '&endCreateDt=20210115'
          )

open_url = url + params
print(open_url)

response = urllib.request.urlopen(open_url)
check = requests.get(open_url)

if check.status_code == 200:
    response_data = response.read()
    soup = bs4.BeautifulSoup(response_data, 'lxml')
    items = soup.find_all("item")

    data = []
    for item in items:
        carecnt = item.find("carecnt").text
        clearcnt = item.find("clearcnt").text
        deathcnt = item.find("deathcnt").text
        decidecnt = item.find("decidecnt").text
        examcnt = item.find("examcnt").text
        resutlnegcnt = item.find("resutlnegcnt").text
        statedt = item.find("statedt").text
        row = [statedt, carecnt, clearcnt, deathcnt, decidecnt, examcnt,resutlnegcnt]
        data.append(row)

    columns = ['기준일','치료중환자수','격리해제수','사망자수','확진자수','검사진행수','결과음성수']
    Corona_data = pd.DataFrame(data=data, columns=columns)
else:
    print("error")

path = os.getcwd()
Corona_data.to_excel(path + "/data/Corona20200401_20210115.xlsx", engine='openpyxl', index=None)

print(Corona_data)
