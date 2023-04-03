smtp_info = dict({'smtp_server' : 'smtp.naver.com', # SMTP 서버 주소
                  'smtp_user_id' : '<송신자(sender) 매일 계정>@naver.com',
                  'smtp_user_pw' : '<송신자(sender) 매일 패스워드>',
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
title = '첨부파일이 있는 파일'
content = '메일 내용입니다.'