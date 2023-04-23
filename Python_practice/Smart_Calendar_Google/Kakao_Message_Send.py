# 일정 주소 네이버 연결할 링크
gaddr_url = 'https://search.naver.com/search.naver?query=' + glocation + '맛집'
# contents 변수를 초기화한다.
contents = []

# 카카오톡 리스트 템플릿을 작성해보자.
template = {
    'object_type' : 'list',
    'header_title' : gsummary + ' - 맛집추천',
    'header_link' : {
        'web_url' : gevent_url,
        'mobile_web_url' : gevent_url
    },
    'contents' : contents,
    'buttons' : [
        {
            'title' : '일정 자세히 보기',
            'link' : {
                'web_url' : gevent_url,
                'mobile_web_url' : gevent_url
            }
        },
        {
            'title' : '일정 장소 보기',
            'link' : {
                'web_url' : gaddr_url,
                'mobile_web_url' : gevent_url
            }
        }
    ],
}


# 카카오톡 리스트 템플릿의 contents를 구성한다.
for place in places:
    ntitle = place.get('title') # 장소 이름
    ncategory = place.get('category') # 장소 카테고리
    ntelephone = place.get('telephone')  # 장소 전화번호
    nlocation = place.get('location')  # 장소 지번 주소

    # 각 장소를 클릭할 때 네이버 검색으로 연결해주기 위해 작성한 코드
    query = nlocation + ' ' + ntitle

    # 장소 카테고리가 카페이면 카페 이미지
    # 이외에는 음식 이미지
    if '카페' in ncategory:
        image_url = 'https://freesvg.org/img/pitr_Coffe_cup_icon.png' # 이미지가 존재하지 않는다고 나온다.
    else:
        image_url = 'https://freesvg.org/img/bentolunch.png?w=150&h=150&fit=fill'

    # 전화번호가 있다면 제목과 함께 넣어주자.
    if ntelephone:
        ntitle = ntitle + '/ntel) ' + ntelephone

    # 카카오톡 리스트 템플릿 형식에 맞춰주자.
    content = {
        'title' : '[' + ncategory + '] ' + ntitle,
        'description' : ' '.join(nlocation.split()[1:]),
        'image_url' : image_url,
        'image_width' : 50, 'image_height' : 50,
        'link' : {
            'web_url' : 'https://search.naver.com/search.naver?query=' + query,
            'mobile_web_url' : 'https://search.naver.com/search.naver?query=' + query
        }
    }
    contents.append(content)

# 카카오톡 메시지 전송
res = kakao_utils.send_message(KAKAO_TOKEN_FILENAME, template)
if res.json().get('result_code') == 0:
    print('일정 맞춤 맛집을 성공적으로 보냈습니다.')
else:
    print('일정 맞춤 맛집을 성공적으로 보내지 못했습니다. 오류메시지 : ', res.json())