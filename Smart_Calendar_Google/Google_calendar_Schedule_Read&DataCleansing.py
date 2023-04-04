# 필요한 라이브러리
from google_auth_oauthlib.flow import InstalledAppFlow
# 구글 캘린더 API 서비스 객체 생성
from googleapiclient.discovery import build
import datetime

# 구글 클라우드 콘솔에서 다운받은 OAuth 2.0 클라이언트 파일 경로
creds_filename = 'google_token.json'
# 사용 권한 지정
# https://www.googleapis.com/auth/calendar
# https://www.googleapis.com/auth/calendar.readonly
SCOPES = ['https://www.googleapis.com/auth/calendar']

# 파일에 담긴 인증 정보로 구글 서버에 인증하기
# 새 창이 열리면서 구글 로그인 및 정보 제공 동의 후 최종 인증이 완료됩니다.
flow = InstalledAppFlow.from_client_secrets_file(creds_filename, SCOPES)
creds = flow.run_local_server(port=0)

### 객체 생성
service = build('calendar', 'v3', credentials=creds)

# 조회에 사용할 요청 변수 지정
calendar_id = 'primary'                     # 사용할 캘린더 ID
today = datetime.date.today().strftime('%Y-%m-%d')
# 일정을 조회할 날짜 YYYY-mm-dd 포맷
time_min = today + 'T00:00:00+09:00'    # 일정을 조회할 최소 날짜
time_max = today + 'T23:59:59+09:00'    # 일정을 조회할 최대 날짜
max_results = 5                         # 일정을 조회할 최대 개수
is_single_events = True                 # 반복 일정의 여부
orderby = 'startTime'                   # 일정 정렬

# 오늘 일정 가져오기
events_result = service.events().list(calendarId = calendar_id,
                                     timeMin = time_min,
                                     timeMax = time_max,
                                     maxResults = max_results,
                                     singleEvents = is_single_events,
                                     orderBy = orderby).execute()

items = events_result.get('items')
print('=====[일정 목록 출력]=====')
print(items)
item = items[0] # 테스트를 위해 오늘 일정해서 한 개만 가져옵니다.

# 일정 제목
gsummary = item.get('summary')

# 일정 제목에서 [식사-성서대]에서 카테고리와 장소를 추출한다.
gcategory, glocation = gsummary[gsummary.index('[')+1 : gsummary.index(']')].split('-')

# 구글 캘린더 일정이 연결되어 있는 링크
gevent_url = item.get('htmlLink')
print('\n\n===== [일정 상세 정보 출력]=====')
print('category : ', gcategory)
print('location : ', glocation)
print('event_url : ', gevent_url)

##########################################################################################################################################

import requests

# 네이버 애플리케이션의 client_id의 client_secret 키 설정
headers = {
    'X-Naver-Client-Id' : "H2yPaJEfeXq9NhNz7TQc",
    'X-Naver-Client-Secret' : "QjbGt6b9e3",
}

# 지역 검색 요청 파라미터 설정
query= glocation + '맛집'
params = {
    'sort' : 'comment',
    'query' : query,
    'display' : 3
}

# 지역 검색 URL과 요청 파라미터
naver_local_url = 'https://openapi.naver.com/v1/search/local.json'

# 지역 검색 요청
res = requests.get(naver_local_url, headers=headers, params=params)

# 지역 검색 결과 확인
places = res.json().get('items')
print(places)