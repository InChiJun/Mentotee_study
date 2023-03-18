import os
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

# 위의 모든 객체를 생성할 수 있는 기본 객체
# MIMEBase(_maintype, _subtype)
# MIMEBase(<메인 타입>, <서브 타입>)
from email.mime.base import MIMEBase

msg_dict = {
    'text' : {'maintype' : 'text', 'subtype' : 'plain', 'filename' : 'res/email_sending/test.txt'}, # 텍스트 첨부파일
    'image' : {'maintype' : 'image', 'subtype' : 'jpg', 'filename' : 'res/email_sending/test.jpg'}, # 이미지 첨부파일
    'audio' : {'maintype' : 'audio', 'subtype' : 'mp3', 'filename' : 'res/email_sending/test.mp3'}, # 오디오 첨부파일
    'video' : {'maintype' : 'video', 'subtype' : 'mp4', 'filename' : 'res/email_sending/test.mp4'}, # 비디오 첨부파일
    'application' : {'maintype' : 'application', 'subtype' : 'octect-stream', 'filename' : 'res/email_sending/test.pdf'}, # 그 외 첨부파일
}