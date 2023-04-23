import requests
import json

# 함수 정의부
def kakao_stt(app_key, stype, data):
    if stype == 'file':
        filename = data
        with open(filename, 'rb') as fp:
            audio = fp.read()
    else:
        audio = data

    headers = {
        'Content-Type': 'application/octet-stream',
        'Authorization': 'KakaoAK ' + app_key,
    }

    # 카카오 음성 url
    kakao_speech_url = 'https://kakaoi-newtone-openapi.kakao.com/v1/recognize'
    # 카카오 음성 api 요청
    res = requests.post(kakao_speech_url, headers=headers, data=audio)
    # 요청에 실패했다면,
    if res.status_code != 200:
        text=''
        print('error! because ',res.json())
    else: # 성공했다면,
        print('음성인식 결과 : ', res.text)
        print('시작위치 : ', res.text.index('{"type":"finalResult"'))
        print('종료위치 : ', res.text.rindex('}')+1)
        print('추출한 정보 : ', res.text[res.text.index('{"type":"finalResult"'):res.text.rindex('}')+1])
        result = res.text[res.text.index('{"type":"finalResult"'):res.text.rindex('}')+1]
        text = json.loads(result).get('value')

    return text

# 함수 호출부
KAKAO_APP_KEY = '<REST_API 앱키를 입력하세요>'
AUDIO_FILE = 'res/jarvis/hello.wav' # 사이트에서 파일을 다운받아야 한다.
text = kakao_stt(KAKAO_APP_KEY, 'file', AUDIO_FILE)
print(text)