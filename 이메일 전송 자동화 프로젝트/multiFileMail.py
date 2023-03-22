smtp_info = dict({'smtp_server' : 'smtp.naver.com', # SMTP 서버 주소
                  'smtp_user_id' : '<송신자(sender) 메일 계정>@naver.com',
                  'smtp_user_pw' : '<송신자(sender) 메일 패스워드>',
                  'smtp_port' : 587}) # SMTP 서버 포트

msg_dict = {
    'text' : {'maintype' : 'text', 'subtype' : 'plain', 'filename' : 'res/email_sending/test.txt'}, # 텍스트 첨부파일
    'image' : {'maintype' : 'image', 'subtype' : 'jpg', 'filename' : 'res/email_sending/test.jpg'}, # 이미지 첨부파일
    'audio' : {'maintype' : 'audio', 'subtype' : 'mp3', 'filename' : 'res/email_sending/test.mp3'}, # 오디오 첨부파일
    'video' : {'maintype' : 'video', 'subtype' : 'mp4', 'filename' : 'res/email_sending/test.mp4'}, # 비디오 첨부파일
    'application' : {'maintype' : 'application', 'subtype' : 'octect-stream', 'filename' : 'res/email_sending/test.pdf'}, # 그 외 첨부파일
}

############################
# 메일 내용 작성
############################
title = '첨부파일이 있는 이메일입니다.'
content = '메일 내용입니다.'
sender = '<송신자(sender) 메일 계정>@naver.com'
receiver = '<수신자(receiver) 메일 주소@naver.com>'

# 이메일 내용
msg = MIMEText(_text = content, _charset = 'utf-8')

# 첨부파일 추가
multi = make_multimsg(msg_dict)
msg['Subject'] = title # 메일 제목
msg['From'] = sender # 송신자
msg['To'] = receiver # 수신자
multi.attach(msg)

# 첨부파일이 추가된 이메일 전송
send_email(smtp_info, multi)