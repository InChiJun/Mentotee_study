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

today = datetime.today().strftime('%Y-%m-%d')
# 일정을 생성할 날짜 YYYY-mm-dd 포맷 ex) today = '2023-04-03'

event = {
    'summary' : '오늘 배워 오늘 쓰는 OpenAPI 수업',
    'location' : '서울특별시 성북구 정릉동 정릉로 77',
    'description' : 'OpenAPI 수업에 대한 설명입니다. 정말 재밌습니다.',
    'start' : {
        'dateTime' : today + 'T10:00:00',
        'timezone' : 'Asia/Seoul',
    },
    'end' : {
        'dateTime' : today + 'T10:00:00',
        'timezone' : 'Asia/Seoul',
    },
    'attendees' : [
        {'email' : 'lpage@example.com'},
        {'email' : 'sbrin@example.com'}
    ],
    'reminders' : {
        'useDefault' : False,
        'overrides' : [
            {'method' : 'email', 'minutes' : 24 * 60},
            {'method' : 'popup', 'minutes' : 10}
        ]
    },
}

# calendarId : 캘린더 ID. primary이 기본 값입니다.
event = service.events().insert(calendarId='primary', body=event).excute()
print('Event created: %s' % (event.get('htmlLink')))