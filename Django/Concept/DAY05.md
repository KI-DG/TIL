# DAY05

### Authentication system

- Authentication (인증)
  - 신원확인
  - 사용자가 자신이 누구인지 확인하는 것
- Authorization ( 권한, 허가)
  - 권한 부여
  - 인증된 사용자가 수행할 수 있는 작업을 결정

#### AUTH_USER_MODEL 

- 프로젝트에서 User를 나타낼 때 사용하는 모델
- 프로젝트가 진행되는 동안 (모델을 만들고 마이그레이션 한 후) 변경할 수 없음

#### custom User model 대체

````python
accounts/models.py
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
	pass

crud/settings.py
AUTH_USER_MODEL = 'accounts.User'

accounts/admin.py
from django.contrib.auth.admin import UserAdmin
from .models import User

admin.site.register(User, UserAdmin)
````

1. 대체할 유저 클래스를 만든다
2. 프로젝트에게 대체할 유저가 이거다라고 알려주기
3. UserAdmin을 등록

[참고]

- AbstractUser
  - 관리자 권한과 함께 완전한 기능을 가지고 있는 User model을 구현하는 추상 기본 클래스
  - 몇 가지 공통 정보를 여러 다른 모델에 넣을 때 사용하는 클래스
  - 데이터베이스 테이블을 만드는 데 사용되지 않으며, 대신 다른 모델의 기본 클래스로 사용되는 경우 해당 필드가 하위 클래스의 필드에 추가 됨

[주의]

- 모델 관계에 영향을 미치기 때문에 훨씬 더 어려운 작업이 필요 
  - 변경사항이 자동으로 수행될 수 없기 때문에 DB 스키마를 직접 수정하고, 이전 사용자 테이블에서 데이터를 이동하고, 일부 마이그레이션을 수동으로 다시 적용해야 함
- 중간 변경은 권장하지 않음 

#### 데이터 베이스 초기화

1. migrations 파일 삭제 
   - 폴더 및 init.py 삭제 금지 
2. db.sqlite3 삭제
3. 다시 migtrations 진행



### HTTP Cookie 

- HTTP
  - 요청
  - 응답
- 특징
  - 비 연결 지향
    - 서버는 요청에 대한 응답을 보낸 후 연결을 끊음
  - 무상태
    - 연결을 끊는 순간 클라이언트와 서버 간의 통신이 끝나며 상태 정보가 유지되지 않음
    - 클라이언트와 서버가 주고받는 메시지들은 서로 완전히 독립적

#### Cookie

- 원리

  - 서버가 사용자의 웹 브라우저에 전송하는 작은 데이터 조각

  - 사용자가 웹사이트를 방문할 경우 해당 웹사이트의 서버를 통해 사용자의 컴퓨터에 설치되는 작은 기록 정보 파일
    - 브라우저는 쿠키를 로컬에 KEY-VALUE의 데이터 형식으로 저장
    - 동일한 서버에 재요청 시 저장된 쿠키를 함꼐 전송

  - 쿠키는 두 요청이 동일한 브라우저에서 들어왔는지 아닌지를 판단할 때 주로 사용
    - 이를 이용해 사용자의 로그인 상태를 유지할 수 있음

- 사용 목적
  1. 세션관리
     - 로그인, 아이디 자동완성, 공지 하루 안보기, 팝업 체크, 장바구니
  2. 개인화
     - 사용자 선호, 테마 등의 설정
  3. 트래킹
     - 사용자 행동을 기록 및 분석

- 세션
  - 클라이언트가 서버에 접속하면 서버가 특정 session id를 발급하고, 클라이언트는 session id를 쿠키에 저장
    - 클라이언트가 다시 동일한 서버에 접속하면 요청과 함께 쿠키를 서버에 전달
  - session id는 세션을 구별하기 위해 필요하며, 쿠키에는 session id만 저장

### Authentication 

- AuthenticationForm

  - 로그인을 위한 built-in form

  #### login

  ```python
  accounts/urls.py
  path('login/', views.login, name='login'),
  
  accounts/views.py
  from django.contrib.auth.forms import AuthenticationForm
  
  def login(request):
      if request.method =='POST':
          pass
      else:
          form = AuthenticationForm()
      context = {
          'form' : form,
      }
      return render(request, 'accounts/login.html', context)
  
  accounts/templates/accounts/login.html
  {% extends 'base.html' %}
  
  {% block content %}
  <h1>LOGIN</h1>
  <form action="{% url 'accounts:login'%}" method="POST">
    {% csrf_token %}
    {{form.as_p}}
    <input type="submit">
  </form>
  {% endblock content %}
  
  accounts/views
  from django.contrib.auth import login as auth_login
  
  def login(request):
      if request.method =='POST':
          form = AuthenticationForm(request.POST)
          if form.is_valid():
              auth_login(request, form.get_user())
              return redirect('articles:index')
      else:
          form = AuthenticationForm()
      context = {
          'form' : form,
      }
      return render(request, 'accounts/login.html', context)
  
  ```

  - get_user()
    - 인스턴스 메서드 
    - 유효성 검사를 통과했을 경우 로그인 한 사용자 객체를 반환

  #### logout

  - 세션을 제거하는 과정 (유저를 삭제하는것은 아님)
  - 사용자가 로그인하지 않은 경우 오류를 발생시키지 않음
  - 2가지 일을 처리
    - 현재 요청에 대한 session data를 DB에서 삭제
    - 클라이언트의 쿠키에서도 session id를 삭제

  ```python
  accounts/urls.py
  path('logout/', views.logout, name='logout'),
  
  accounts/views.py
  from django.contrib.auth import logout as auth_logout
  def logout(request):
      auth_logout(request)
      return redirect('articles:index')
  
  base.html
  <form action="{% url 'accounts:logout' %}" method="POST">
        {% csrf_token %}
        <input type="submit" value="Logout">
      </form>
  ```

  

### 회원가입

- UserCreationForm
  - ModelForm
- 3개의 필드를 가짐
  - username
  - password1
  - password2

```python
accounts/urls.py
path('signup/', views.signup, name='signup'),

accounts/views.py
def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('articles:index')
    else:
        form = UserCreationForm()
    context ={
        'form': form
    }
    return render(request, 'accounts/singup.html', context)

./accounts/singup.html
{% extends 'base.html' %}

{% block content %}
<h1>회원가입</h1>
<form action="{% url 'accounts:singup' %}" method="POST">
  {% csrf_token %}
  {{form.as_p}}
  <input type="submit">
</form>
{% endblock content %}
```

```python
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

class CustomUserCreation(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = get_user_model()
# 장고는 User(model.py)를 직접 가지고 오는것을 선호하지 않음
```



### 회원탈퇴

- DB에서 유저를 Delete하는 것과 같음

```python
accounts/urls.py
path('delete/', views.delete, name='delete'),

accounts/views.py
def delete(request):
    request.user.delete()
    return redirect('articles:index')

base.html
 <form action="{% url 'accounts:delete' %}" method="POST">
      {% csrf_token %}
      <input type="submit" value="회원탈퇴">
```

### 회원수정

- User를 Update 하는 것이며 UserChangeForm 을 사용

#### UserChangeForm

- 사용자의 정보 및 권한을 변경하기 위해 admin 인터페이스에서 사용되는 ModelForm 
- UserChangeForm 또한 ModelForm이기 때문에 instance인자로 기존 user 데이터 정보를 받는 구조 또한 동일
- CustomUserChangeForm을 사용

```python
accounts/urls.py
path('update/', views.update, name='unpdate'),

accounts/views.py
def update(request):
    if request.method == "POST":
        form = CustomUserchangeForm(request.POST, instnace=request.user)
        if form.is_valid():
            form.save()
        return redirect('articles:index')
    else:
        form = CustomUserchangeForm(instance=request.user)
    context ={
        'form' : form,
    }
    return render(request, 'accounts/update.html', context)

accounts/update.html
{% extends 'base.html' %}

{% block content %}
<h1>회원정보수정</h1>
<form action="{% url 'accounts:update' %}" method="POST">
  {% csrf_token %}
  {{form.as_p}}
  <input type="submit">
</form>
{% endblock content %}
```

- 문제점
  - 일반 사용자가 접근해서는 안될 정보들(fields)까지 모두 수정이 가능해짐
  - 상속받아 작성해 두었던 서브클래스 CustomUserChangeForm에서 접근 가능한 필드를 조정

#### PasswordChangeForm

- 사용자가 비밀번호를 변경할 수 있도록 하는 Form
- 이전 비밀번호를 입력하여 비밀번호를 변경할 수 있도록 함

암호 변경 시 세션 무효화 방지하기

- 비밀번호가 변경되면 기존 세션과의 회원 인증 정보가 일치하지 않게 되어버려 로그인 상태가 유지되지 못함
- 비밀번호는 잘 변경되었으나 비밀번호가 변경되면서 기존 세션과의 회원 인증 정보가 일치하지 않기 때문
- update_session_auth_hash()
  - update_session_auth_hash(request, user)
  - 현재 요청과 새 session data가 파생 될 업데이트 된 사용자 객체를 가져오고, session data를 적절하게 업데이트해줌
  - 암호가 변경되어도 로그아웃 되지 않도록 새로운 password의 session data로 session 업데이트

### Limiting access to logged-in users

- 로그인 사용자에 대한 접근 제한하기

#### is_authenticated

- 사용자가 인증 되었는지 여부를 알 수 있는 방법
- 모든 User 인스턴스에 대해 항상 True인 읽기 전용 속성
- 일반적으로 request.userdptj dlthrtjddmf tkdyd 
- 로그인된 사용자인지 비로그인 사용자인지만 확인
- 권한과는 관련이 없으며, 사용자가 활성화 상태이거나 유효한 세션을 가지고 있는지도 확인하지 않음