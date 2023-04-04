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