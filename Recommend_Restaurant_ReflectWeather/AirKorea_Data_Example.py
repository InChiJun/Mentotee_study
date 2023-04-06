import requests
import json
import datetime

dust_url = 'http://apis.data.go.kr/B552584/ArpltnInforInqireSvc/getCtprvnRltmMesureDnsty?'

service_key = 'VIqxEFRYT4zZpNNVDiZ7GWJMfTw3h%2FVmKCkQ7ivS8G%2BOfGlxzwl6Mb65rq70tqMRbR918sDVhGOuxTTSTYY8gw%3D%3D'

payload = 'serviceKey=' + service_key + '&' + \
    'returnType=json' + '&' + \
    'sidoName=서울' + '&' +\
    'ver=1.0'

# pm10과 pm2.5 수치 가져오기
res = requests.get(dust_url + payload)
result = res.json()
dust = dict()
if (res.status_code == 200) & (result['response']['header']['resultCode'] == '00'):
    dust['PM10'] = {'value' : int(result['response']['body']['items'][0]['pm10Value'])}
    dust['PM2.5'] = {'value' : int(result['response']['body']['items'][0]['pm25Value'])}
else:
    print('미세먼지 가져오기 실패 : ', result['response']['header']['resultMsg'])

print(dust)