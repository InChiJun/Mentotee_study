from email.mime.text import MIMEText

smtp_info = dict({'smtp_server' : 'smtp.naver.com', # SMTP 서버 주소
                  'smtp_user_id' : '<송신자(sender) 매일 계정>@naver.com',
                  'smtp_user_pw' : '<송신자(sender) 매일 패스워드>',
                  'smtp_port' : 587}) # SMTP 서버 포트

# 메일 내용 작성
title = '기본 이메일입니다.'
content = '메일 내용입니다.'
sender = smtp_info['smtp_user_id'] # 송신가(sender) 이메일 계정
receiver = '<수신자(receiver) 메일 주소>@naver.com'

# 메일 객체 생성 : 메시지 내용에는 한글이 들어가기 때문에 한글을 지원하는 문자 체계인 UTF-8을 명시하여 준다.
msg = MIMEText(_text = content, _charset = 'utf-8') # 이메일 내용

msg['Subject'] = title # 메일 제목
msg[''] = sender # 송신자
msg[''] = receiver # 수신자

send_email(smtp_info, msg)