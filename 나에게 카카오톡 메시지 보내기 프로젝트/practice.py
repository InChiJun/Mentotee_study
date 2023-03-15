import requests

url = "https://kauth.kakao.com/oauth/token"

data = {
    "grant_type" : "authorization_code",
    "client_id" : "1b1f5d3ec45c1d9534b4b824fb7f697d",
    "redirect_uri" : "http://localhost.com",
    "code" : "_S8RHbLx57Wf-7lybbAN6DVuTUKkYvXxVoImTTKwrFGMf18tCTIlykhw-jOLztFcfV0oqwo9c-sAAAGGyw62gA"
}

response = requests.post(url, data=data)

# 요청에 실패했다면,
if response.status_code != 200:
    print("error! because ", response.json())
else: # 성공했다면,
    tokens = response.json()
    print(tokens)