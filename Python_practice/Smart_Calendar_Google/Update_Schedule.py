event = events_result.get('items')[0]
event_id = event.get('id')

# 원하는 일정의 속성 값 변경하기
event['summary'] = '(수정된)' + event['summary']

# 일정 수정 요청하기
updated_event = service.events().update(calendarId='primary', eventId=event_id, body=event).execute()