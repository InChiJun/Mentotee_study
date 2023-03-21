import os
import smtplib
import sys
reload(sys)
sys.setdefaultencoding('utf8')

# 이메일 메시지에 다양한 형식을 중첩하여 담기 위한 객체
from email.mime.multipart import MIMEMultipart

# 이메일 메시지를 이진 데이터로 바꿔주는 인코더
from email import encoders

# 텍스트 형식
from email.mime.text import MIMEText
# 이미지 형식
from email.mime.image import MIMEImage
# 오디오 형식
from email.mime.audio import MIMEAudio

# 위의 모든 객체들을 생성할 수 있는 기본 객체
# 위의 모든 객체를 생성할 수 있는 기본 객체
# MIMEBase(_maintype, _subtype)
# MIMEBase(<메인 타입>, <서브 타입>)
from email.mime.base import MIMEBase

def send_mail(smtp_info, msg):
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

def make_multimsg(msg_dict):
    multi = MIMEMultipart(_subtype='mixed')

    for key, value in msg_dict.items():
        # 각 타입에 적절한 MIMExxx() 함수를 호출하여 msg 객체를 생성한다.
        if key == 'text':
            with open(value['filename'], encoding='utf-8') as fp:
                msg = MIMEText(fp.read(), _subtype=value['subtype'])
        elif key == 'image':
            with open(value['filename'], 'rb') as fp:
                msg = MIMEImage(fp.read(), _subtype=value['subtype'])
        elif key == 'audio':
            with open(value['filename'], 'rb') as fp:
                msg = MIMEAudio(fp.read(), _subtype=value['subtype'])
        else:
            with open(value['filename'], 'rb') as fp:
                msg = MIMEBase(value['maintype'], _subtype=value['subtype'])
                msg.set_payload(fp.read())
                encoders.encode_base64(msg)
        # 파일 이름을 첨부파일 제목으로 추가
        msg.add_header('Content-Disposition', 'attachment',
                       filename=os.path.basename(value['filename']))
        # 첨부파일 추가
        multi.attach(msg)

    return multi

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