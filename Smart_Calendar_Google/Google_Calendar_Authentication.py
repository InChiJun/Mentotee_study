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

####################################################################################################################################

today = datetime.datetime.today().strftime('%Y-%m-%d')
# 일정을 생성할 날짜 YYYY-mm-dd 포맷 ex) today = '2023-04-04'

event = {
    'summary' : '오늘 배워 오늘 쓰는 OpenAPI 수업', # 일정 제목
    'location' : '서울특별시 성북구 정릉동 정릉로 77', # 일정 장소
    'description' : 'OpenAPI 수업에 대한 설명입니다. 정말 재밌습니다.', # 일정 설명
    'start' : { # 시작 날짜
        'dateTime' : today + 'T10:00:00',
        'timeZone' : 'Asia/Seoul',
    },
    'end' : { # 종료 날짜
        'dateTime' : today + 'T10:00:00',
        'timeZone' : 'Asia/Seoul',
    },
    'attendees' : [ # 참석자
        {'email' : 'lpage@example.com'},
        {'email' : 'sbrin@example.com'}
    ],
    'reminders' : { # 알림 설정
        'useDefault' : False,
        'overrides' : [
            {'method' : 'email', 'minutes' : 24 * 60}, # 24 * 60분 = 하루 전 알림
            {'method' : 'popup', 'minutes' : 10} # 10분 전 알림
        ]
    },
}

# calendarId : 캘린더 ID. primary이 기본 값입니다.
event = service.events().insert(calendarId='primary', body=event).execute()
print('Event created: %s' % (event.get('htmlLink')))

####################################################################################################################################

# 조회에 사용할 요청 변수 지정
calendar_id = 'primary'                     # 사용할 캘린더 ID
today = datetime.date.today().strftime('%Y-%m-%d')
# 일정을 조회할 날짜 YYYY-mm-dd 포맷
time_min = today + 'T00:00:00+09:00'    # 일정을 조회할 최소 날짜
time_max = today + 'T23:59:59+09:00'    # 일정을 조회할 최대 날짜
max_results = 5                         # 일정을 조회할 최대 개수
is_single_events = True                 # 반복 일정의 여부
orderby = 'startTime'                   # 일정 정렬

events_result = service.events().list(calendarId = calendar_id,
                                     timeMin = time_min,
                                     timeMax = time_max,
                                     maxResults = max_results,
                                     singleEvents = is_single_events,
                                     orderBy = orderby
                                     ).execute()

items = events_result.get('items')
print('=====[일정 목록 출력]=====')
print(items)

####################################################################################################################################

event = events_result.get('items')[0]
event_id = event.get('id')

# 원하는 일정의 속성 값 변경하기
event['summary'] = '(수정된)' + event['summary']

# 일정 수정 요청하기
updated_event = service.events().update(calendarId='primary', eventId=event_id, body=event).execute()

####################################################################################################################################

# eventId : 일정을 조회한 후 얻은 id값을 의미한다.
eventId = updated_event.get('id')
service.events().delete(calendarId='primary', eventId=eventId).execute()