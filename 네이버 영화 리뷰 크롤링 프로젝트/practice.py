from bs4 import BeautifulSoup

html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters;
and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""

# BeautifulSoup 객체 생성
soup = BeautifulSoup(html_doc, "lxml")

# 객체.태크이름
# .태그 이름으로 하위 태그로의 접근이 가능하다.
print("soup.body.p의 결과 : ", soup.body.p)

# 객체.태그['속성 이름']
# 객체의 태그 속성은 파이썬 딕셔너리처럼 태그['속성 이름']으로 접근이 가능하다.
print("soup.a['href']의 결과", soup.a['href'])

# 객체.name
## name 변수
print('soup.title.name의 결과 : ', soup.title.name)

# 객체.string
## string 변수 (참고) NavigableString: 문자열은 태그 안의 텍스트에 상응한다. BeautifulSoup은 이런 텍스트를 포함하는 NavigableString 클래스를 사용한다.
print('soup.title.string의 결과 : ', soup.title.string)

# 객체.contents
## 태그의 자식을을 리스트로 변환
print("soup.contents의 결과 : ", soup.contents)

# find() : 태그 하나만 가져옴
'''
find(name, attrs, recursive, string, **kwargs)

[옵션]
name - 태그 이름
attrs - 속성(딕셔너리로)
recursive - 모든 자식 or 자식
string - 태그 안에 텍스트
keyword - 속성(키워드로)

* (주의) class는 파이썬 예약어이므로, class_를 사용한다.
'''
print("soup.find()의 결과 : ", soup.find('a', attrs={'class' : 'sister'}))

# find_all() : 해당 태그가 여러 개 있을 경우 한꺼번에 모두 가져온다. 그 객체들의 리스트로 반환한다.
'''
find_all(name, attrs, recursive, string, limit, **kwargs)

[옵션]
Limit -몇 개까지 찾을 것인가? find_all()로 검색했을 때,  수천, 수만 개가 된다면 시간이 오래 걸릴 것이다. 이때 몇 개까지만 찾을 수 있도록 제한을 둘 수 있는 인자이다.
'''
print("soup.find_all()의 결과 : ", soup.find_all('a', limit=2))