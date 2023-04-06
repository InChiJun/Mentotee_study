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