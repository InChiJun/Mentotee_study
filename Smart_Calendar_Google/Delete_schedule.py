# eventId : 일정을 조회한 후 얻은 id값을 의미한다.
eventId = updated_event.get('id')
service.events().delete(calendarId='primary', eventId=eventId).execute()