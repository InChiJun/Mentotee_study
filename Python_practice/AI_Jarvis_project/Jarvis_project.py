import jarvis_food_recommender
import jarvis_stock_report

KAKAO_APP_KEY = '<REST_API 앱 키를 입력하세요.>'

KEYWORD_STOCK = '주식'
KEYWORD_WEATHER = '날씨'

# 음성 수집
audio = get_speech()

# STT
command = kakao_stt(KAKAO_APP_KEY, 'stream', audio)
print('명령어 : ' + command)
print('명령을 수행합니다.')

# 음성 분석
if KEYWORD_WEATHER in command:
    print('날씨를 파악하여 맛집을 추천합니다.')
    jarvis_food_recommender.do()
elif KEYWORD_STOCK in command:
    print('주식 보고서를 메일로 전송합니다.')
    jarvis_stock_report.do()
else:
    print('명령을 알 수 없습니다.')