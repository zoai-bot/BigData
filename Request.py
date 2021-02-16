import requests, bs4
import pandas as pd
import urllib.request
import xmltodict
import json
from urllib.request import Request, urlopen
from urllib.parse import urlencode, quote_plus, unquote

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
print(check)
response_data = response.read()

dic_data = xmltodict.parse(response_data)
j_data = json.dumps(dic_data)
print(j_data)
# data = json.loads(j_data)
# print(data.get("decideCnt"))


# response = urllib.request.urlopen(open_url)
# print(response)
#
# data = response.read()
#
# soup = bs4.BeautifulSoup(response, 'lxml')
# print(soup)
#
# bunch = soup.find_all('items')
# print(bunch)
# #2020년4월 1일부터 2021년 1월15일 data
# data = pd.DataFrame(columns=['기준일','확진자수','격리해제 수','사망자 수', '결과 음성 수'])


#
# result = requests.get(url + queryParams)
# js = json.loads(result.content)
# data = pd.DataFrame(js['response']['body']['items']['item'])
#
# li = ['stnId','tm','avgTa','minTa','maxTa','sumRn','maxWs','avgWs','ddMes']
#
# data.loc[:,li]
#
# data[li].to_csv("weather.csv",index=False )