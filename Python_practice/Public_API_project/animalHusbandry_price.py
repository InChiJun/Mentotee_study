import requests
import pprint
import json

url = "https://apis.data.go.kr/1390906/nias_gong_api1/getList_api1?serviceKey=VIqxEFRYT4zZpNNVDiZ7GWJMfTw3h%2FVmKCkQ7ivS8G%2BOfGlxzwl6Mb65rq70tqMRbR918sDVhGOuxTTSTYY8gw%3D%3D&pageNo=1&numOfRows=10&type=json"

response = requests.get(url)

contents = response.content


# pp = pprint.PrettyPrinter(indent=4)
# print(pp.pprint(contents))
#
json_ob = json.loads(contents)
pprint.pprint(json_ob)
# print(type(json_ob))