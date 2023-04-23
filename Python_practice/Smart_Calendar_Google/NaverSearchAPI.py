import requests

# 네이버 애플리케이션의 client_id의 client_secret 키 설정
headers = {
    'X-Naver-Client-Id' : "H2yPaJEfeXq9NhNz7TQc",
    'X-Naver-Client-Secret' : "QjbGt6b9e3",
}

# 지역 검색 요청 파라미터 설정
query='성서대 맛집'
params = {
    'sort' : 'comment',
    'query' : query,
    'display' : 3
}

# 지역 검색 URL과 요청 파라미터
naver_local_url = 'https://openapi.naver.com/v1/search/local.json'

# 지역 검색 요청
res = requests.get(naver_local_url, headers=headers, params=params)
if res.status_code == 200:
    # 지역 검색 결과 확인
    places = res.json().get('items')
    print(places)