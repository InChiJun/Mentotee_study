import requests
import json
import datetime

village_weather_url = 'http://apis.data.go.kr/1360000/VilageFcstInfoService_2.0/getVilageFcst?'

service_key = 'VIqxEFRYT4zZpNNVDiZ7GWJMfTw3h%2FVmKCkQ7ivS8G%2BOfGlxzwl6Mb65rq70tqMRbR918sDVhGOuxTTSTYY8gw%3D%3D'
base_date = datetime.datetime.today().strftime('%Y%m%d') # '20230405' == 기준 날짜
base_time = '0800' # 기준 시간
nx = '59'
ny = '126'

payload = 'serviceKey=' + service_key + '&' +\
    'dataType=json' + '&' +\
    'base_date=' + base_date + '&' +\
    'base_time=' + base_time + '&' +\
    'nx=' + nx + '&' +\
    'ny=' + ny

pty_code = {'0': '없음', '1': '비', '2': '비/눈', '3': '눈', '4': '소나기', '5': '빗방울', '6': '빗방울/눈날림', '/': '눈날림'}

data = dict()
data['data'] = base_date
weather = dict()

# 값 요청
res = requests.get(village_weather_url + payload)
try:
    items = res.json().get('response').get('body').get('items')
    for item in items['item']:
        # 기온
        if item['category'] == 'TMP':
            weather['tmp']
    print(items)
except:
    print('날씨 정보 요청 실패 : ', res.text)