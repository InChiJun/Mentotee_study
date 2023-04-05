import json
import kakao_utils

KAKAO_TOKEN_FILENAME = '../kakao_token.json'
KAKAO_APP_KEY = "1b1f5d3ec45c1d9534b4b824fb7f697d"
kakao_utils.update_tokens(KAKAO_APP_KEY, KAKAO_TOKEN_FILENAME)

a = 3
arr = []