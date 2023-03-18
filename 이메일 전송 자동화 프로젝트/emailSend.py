import smtplib

smtp_info = dict({'smtp_server' : 'smtp.naver.com', # SMTP 서버 주소
                  'smtp_user_id' : '<송신자(sender) 매일 계정>@naver.com',
                  'smtp_user_pw' : '<송신자(sender) 매일 패스워드>',
                  'smtp_port' : 587}) # SMTP 서버 포트

def send_email(smtp_info, msg):
    with smtplib.SMTP(smtp_info['smtp_server'], smtp_info['smtp_port']) as server:
        # TLS 보안 연결
        server.starttls()
        # 로그인
        server.login(smtp_info['smtp_user_id'], smtp_info['smtp_user_pw'])
        # 로그인 된 서버에 이메일 전송
        response = server.sendmail(msg['from'], msg['to'], msg.as_string())
        # 메시지를 보낼 때는 .as_string() 메서드를 사용해서 문자열로 바꿔준다.

        # 이메일을 성공적으로 보내면 결과는 {}
        if not response:
            print('이메일을 성공적으로 보냈습니다.')
        else:
            print(response)