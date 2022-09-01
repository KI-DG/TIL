# DAY01

## Django

- 로그인, 로그아웃, 회원관리, 데이터베이스, 서버, 클라이언트, 보안 - 너무 많은 기술들이 필요
- 잘 만들어 진 것들을 가져다가 좋은 환경에서 잘 쓰기만 하면 되는 세상 - 바닥부터 하지 말고 있는 걸 사용하자!

#### Framework

- ex) == 밀키트 (자유도는 떨어지지만 기본은 한다)
- 서비스 개발에 필요한 기능들을 미리 구현해서 모아 놓은 것 

- 스타트 업에서 많이 사용
- 하나부터 열까지 직접 개발할 필요 없이, 내가 만들고자 하는 본질에 집중해 개발할 수 있음

1. 배워야 하는 이유 

   - python으로 작성된 프레임 워크
     - python이라는 언어의 강력함과 거대한 커뮤니티

   - 수많은 여러 유용한 기능들 (공식 사이트가 잘되어 있음)

#### WWW

- 전 세계에 퍼져 있는 거미줄 같은 연결망

#### 클라이언트 - 서버

- 클라이언트 - 서버 구조 (요청 - 응답)
- 클라이언트(Chrome 또는 Firefox 같은 웹 브라이저) 서비스를 요청하는 주체 (**나**)
- 서버(웹 페이지, 사이트 또는 앱을 저장하는 컴퓨터) 요청에 대해 서비스를 응답하는 주체

#### 정적 페이지 , 동적 페이지

- 정적 페이지 - 있는 그대로 제공하는 것 변하지 않는 것
- 동적 페이지 - 웹페이지의 내용을 바꿔 주는 주체 == 서버 
  - 사용자의 요청을 받아서 적절한 응답을 만들어 주는 프로그램을 쉽게 만들 수 있게 도와주는 프레임 워크가 Django

#### Design Pattern

- 자주 사용하는 패턴이 있다 == 일반화해서 하나의 공법으로 만들어 둔 것 

##### 소프트웨어 디자인 패턴

- 클라이언트 - 서버 구조도 소프트웨어 디자인 패턴 중 하나

- 장점
  - 빠른 의사소통과 빠른 처리를 할 수 있다

#### Django`s Design Pattern

이거 모르면 쓸 수가 없다

##### MVC패턴 (전통적인 디자인 패턴, 자바)

- Model - View - Controller의 준말

- 데이터 - 화면 - 둘을 연결 

##### MTV패턴(Django)

- Model - Template - View
- 데이터 - 화면 - 둘을 연결
- Model
  -  == MVC의 Model 역할
  - 데이터와 관련된 로직
  - 응용프로그램의 데이터 구조를 정의하고 데이터베이스의 기록을 관리
- Template 
  - == MVC의 View 역할
  - 레이아웃과 화면을 처리
  - 사용자에게 직접적으로 보여 주는 화면에 해당
- View
  - == MVC의 Controller 역할
  - Modle ＆Template과 관련한 로직을 처리해서 응답을 반환
  - 데이터가 필요하다면  model에 접근해서 데이터를 가져오고, 가져온 데이터를 template로 보내 화면을 구성하고, 구성된 화면을 응답으로 만들어 클라이언트에게 반환

① 요청

② URL

③ 응답 

④ 데이터 가져온다

⑤ 화면에 보여 준다

----------

정리 

디자인 패턴이 있다

우리는 Django을 통해 디자인 패턴을 구상한다

그게 MTV인데 MTV는 다섯 가지로 이뤄질 수 있다

① 요청 ② URL ③ 응답 ④ 데이터 가져온다 ⑤ 화면에 보여 준다

---------

#### 사용 방법

1. venv의 환경을 만들어 준다. - venv (가상 환경)
   - python -m venv venv 

2. venv를 활성화 시켜 준다. 

   - source venv/Scripts/activate (window 용)

   - source venv/bin/activate (mac에서 사용)
   - tip) tab을 누르면 자동 완성됨

3. 가상 환경 비활성화 하는 법

   - deactivate

4. django 설치

   - pip install django==3.2.13

5.  가상 환경 패키지 목록 조회

   - pip list

6. requirements.txt 생성

   - pip freeze>requirements.txt 

   1. 하는 이유 (용량이 크다.) - venv는 로컬에서만 사용 // github에 올리지 말자!
      1. 가상 환경에 들어갈 패키지 목록을 저장하는 역할 
      2. 다른데 가서 설치할 때 편하게 하기 위해서 (requirements.txt)
   2. 사용 방법
      1. python -m venv venv
      2. source venv/Scripts/activate
      3. pip install - r requirements.txt
      4. 만약 다른 것을 더 설치 하였으면 pip freeze>requirements.txt 명령어를 입력해서 덮어써 준다

7. django 프로젝트 생성

   - django-admin startproject firstpjt . 
   - .을 안 하면 폴더가 중첩인 된다   '.'은 현재 폴더을 의미해서

8. django 서버 실행

   - python manage.py runserver

   1. 새로운 터미널로 안 나가짐 서버가 켜져 있어서 Ctrl + c 누르면 꺼짐

9. 구조 

   1. 프로젝트 (firstpjt)
   2. articles(게시 글, 영화 관련 정보를 띄어 주는 애플리케이션), accounts(사용자 담당 애플리케이션) 
   3. 애플리케이션이 모이면 프로젝트가 완성

10. django 애플리케이션 생성

    - python manage.py startapp articles
    - 관례 - 복수형으로 한다.

11. INSTALLED_APPS에 앱을 등록 

    1. firstpjt - settings.py - INSTALLED_APPS에 첫번째로 지정 
    2. 사용자 지정 앱은 첫번째에 저장 해야 된다
    3. 앱을 생성하고 저장한다 (이렇게 안 하면 앱이 등록이 안 된다)

12. URL 생성 (순서대로 해야된다.)

    1. firstpjt - urls.py - urlpatterns(메뉴판)
    2. path('index/', views.index), - url 끝에는 / 가 꼭 들어가야 된다.
    3. 마지막에는 ',' 가 꼭 들어가야 된다.(확장성)
    4. from articles import views
    5. 'index/', views.index (메뉴판 , 레시피)

13. Views 생성

    ```pthyon
    firstpjt -views.py 에 함수 생성
    요청 개체 무조건 먼저 나와야 된다.
    def index(request):
    
      return render(request, 'index.html')
    ```

14. Templates 생성

    1. ! + tab

15. Material Icon Theme

----------------------

LTS(자기 지원 버전)

3.2 버전

```python
__init__.py - 파이썬 패키지로 다루기 위해 (하위버전을 위해 넣어준다)
asgi.py - 비동기식 처리
settings.py - 프로젝트 설정
urls.py - urls 생성 (views의 연결의 지정)
wsgi.py - 동기식 처리 
manage.py - 전체 프로젝트의 관리자

admin.py - 관리자 페이지
models.py - MTV 패턴의 m 
tests.py - 테스트 코드를 작성하는 곳
views.py - MTV 패턴의 V 
```

```python
INSTALLED_APPS = [
    # Local appps
    사용자 지정함수
    # Third party apps
    
    # Django apps 
]
```

수업에는 상관없지만 추후 advanced한 내용을 대비 

```python
LANGUAGE_CODE = 'ko-kr' (언어를 한국어로 바꿔줄 수 있다)

TIME_ZONE = 'Asia/Seoul' (한국시간으로 바꿔줄수 있다)

USE_I18N = True (위에 언어 설정이 적용되려면 True로 되어있어야 된다) - 번역 시스템을 활성화해야 하는지 여부를 지정 

USE_TZ = True (위에 시간 설정이 적용되려면 True로 되어있어야 된다)

I18N (internationalization - 국제화 i다음 18자 n를 의미)
L10N (localizaion - 현지화 l다음 10자 n를 의미)
```

---------------

#### DTL 

- 프로그래밍적 로직이 아니라 프레젠테이션을 표현하기 위한 것임을 명심할 것

```html
Variable
def greeting(request):
    context ={
        'name': 'justin',
        'foods': ['apple', 'chicken', 'burger'],
    }
    return render(request, 'greeting.html', context)
context에 무조건 넣어서 사용해준다
<h1>안녕하세요 저는 {{name}} 입니다</h1>
{{}} 두개로 사용해준다

Filters
<p>제 이름의 길이는 {{name|length}} 글자 입니다</P>
\ 엔터 위에 키를 이용해 Filters를 사용할 수 있다

Tags
{% for food in foods %}
  {% if food|length > 6  %}
    <p>{{food}}</p>
  {% endif %}
{% endfor %}

{% for  in  %}{% endfor %} 이 사이에 넣어서 for문 사용 if문도 동일

Comments
{#<p>이것은 주석입니다</p>#}
{% comment %}
<p>이것은 여러줄 주석입니다</p>
<p>이것은 여러줄 주석입니다</p>
{% endcomment %}

views.py 에서
def greeting(request):
    foods = ['apple', 'chicken', 'burger']
    six_food = [food for food in foods if len(food) > 6]
    
    context ={
        'name': 'justin',
        'foods': foods,
        'six_food': six_food,
    }
    return render(request, 'greeting.html', context)

greeting.html 에서
<p>6글자 초과의 음식은 {{six_food}}</p>
  {% comment %} # 개발자는 위에처럼 사용 {% endcomment %}
  {% comment %} {% for food in foods %}
    {% if food|length > 6 %}
      <p>6글자 초과의 음식은 {{food}}</p>
    {% endif %}
  {% endfor %} {% endcomment %}  
  {% comment %} # 개발자가 하는건 아니다 디자이너의 영역 {% endcomment %}

```

#### Template inheritance(상속)

- 코드의 재 사용성에 초점을 맞춤

- extneds
  -  하나만 상속 받을 수 있다. 최상단에서만 작성되어야 된다
- block
  - 하위 템플릿에 재지정할 수 있는 블록을 정의 
  - endblock 태그에 이름을 지정할 수 있다 (가독성을 높이기 위해)

```python
BASE_DIR = Path(__file__).resolve().parent.parent
# 지금 Path(__file__).resolve() 코드가 쓰인 파일의 절대 경로 


TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
	  **'DIRS': [BASE_DIR / 'templates',],** # 이렇게 추가 해준다
```



#### Sending form data

- action 
  - 입력 데이터가 전송될 URL 

- method
  - 데이터를 어떻게 보낼 것인지 정의 
  - HTTP -  프로토콜 == 규약(약속)
    - GET방식 - 조회
    - POST방식 - 생성
    - PUT - 바꾸는 것
    - DELETE - 삭제하는 것(회원탈퇴, 게시물 삭제)



#### Trailing URL Slashes

Django는 URL 끝에 /가 없다면 자동으로 붙여주는 것이 기본 설정

- 그래서 모든 주소가'/'로 끝나도록 구성 되어있음

#### Varible routing 

- URL 주소를 변수로 사용하는 것을 의미
- URL의 일부를 변수로 지정하여 view 함수의 인자로 넘길 수 있음
- 변수 값에 따라 하나의 path()에 여러 페이지를 연결 시킬 수 있음

```python
urls.py
path('show/<str:name>/', views.show) #name 은 변수같은거 <타입 : 변수> 정수(int)도 사용가능 str(은 생략해도 됨)

views.py
def show(request, name):
    context = {
        'name': name
    }
    return render(request, 'show.html', context)

show.html
{% extends 'base.html' %}

{% block content %}
  <h1>{{name}}</h1>
{% endblock content %}
```

#### URL mapping

URL이 많을 때 매핑하는 방법

페이지가 많을 때 각자에다가 urls.py를 넣는다.

```python
fistpjt/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('articles/', include('articles.urls')),    
    path('pages/', include('pages.urls')),
]

articles/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index),
    path('greeting/', views.greeting),
    path('throw/', views.throw),
    path('catch/', views.catch),
    path('lotto/', views.lotto),
]

pages/urls.py
from django.urls import path
from . import views

urlpatterns = []

```

#### Naming URL patterns

```python
from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index, name = 'index'),
    path('greeting/', views.greeting, name = 'greeting'),
    path('throw/', views.throw, name = 'throw'),
    path('catch/', views.catch, name = 'catch'),
    path('lotto/', views.lotto, name = 'lotto'),
]

<a href={% url 'throw' %}> 다시 던지러가자.</a>
<a href={% url 'index' %}> 홈화면으로 이동.</a>
<a href={% url 'index' %}> 홈화면으로 이동.</a>
```

Django Windows Python Vsc
