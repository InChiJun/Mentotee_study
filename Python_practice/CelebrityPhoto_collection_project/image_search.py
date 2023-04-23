import requests
import json

#이미지 검색
url = 'https://dapi.kakao.com/v2/search/images'
headers = {
    'Authorization' : 'KakaoAK <REST_API 앱 키를 입력하세요'
}
data = {
    'query' : '펭수'
}

# 이미지 검색 요청
response = requests.post(url, headers=headers, data=data)
# 요청에 실패했다면,
if response.status_code != 200:
    print('error! because ', response.json())
else: # 성공했다면,
    count = 0
    for image_info in response.json()['documents']:
        print(f'[{count}th] image_url =', image_info['image_url'])
        # 저장할 이미지 파일명 설정
        count += 1