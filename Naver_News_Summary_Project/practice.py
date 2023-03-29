import requests
# 해당 분야 상위 뉴스 HTML 가져오기

headers = {'User-Agent' : '<복사한 user-agent 값 대체>'}
# ex. 'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) ...생략...'

res = requests.get(news_link, headers = headers)
print(res.text)




# for sid in ['100', '101', '102']:
#     # 해당 분야 상위 뉴스 목록 주소
#     sec_url = 'https://news.naver.com/main/main.naver?mode=LSD&mid=shm ' \
#         + '&sId1=' \
#         + sid \
#
#     print('section url : ', sec_url)