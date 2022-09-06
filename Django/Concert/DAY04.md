# DAY04

## Django Form

- 우리가 원하는 데이터형식에 맞는지에 대한 유효성 검증이 필요 

- Django Form은 이과정에서 과중한 작업과 반복 코드를 줄여줌으로써 훨씬 쉽게 유효성 검증을 진행할 수 있도록 만들어 줌

### Form class 선언

Model과 마찬가지로 상속을 통해 선언

```python
forms.py 만들고 

from django import forms 불러와주고 

class ArticleForm(forms.Form):
title = forms.CharField(max_length=10)  # max_length 는 필수는 아님 
content = forms.CharField() # textField는 존재하지 않음

views.py
def new(request):
    form = ArticleForm()
    context ={
        'form' : form
    }
    return render(request, 'articles/new.html', context)

new.html
{{form}}
```

- form.as_p == 줄바꿈 (각각의 p태그로 감싸줌)
- as_ul == 각 필드가 < li>태그로 감사찜 , 태그는 직접 작성

​	Form  fields에서 컨드롤 해줘야된다

- textarea로 바꾸려면 widgets (표현만 바꿔줌) 
  - input 요소의 단순한 출력 부분을 담당 
  - form fields에 할당됨

​	widgets

- 단순히 HTML 랜더링을 처리하는 것이며 유효성 검증과 아무런 관계가 없음

### ModelForm

중복이 너무 많이되는데?

ModelFOrm을 사용하면 이러한 Form을 더 쉽게 작성

Form Class를 만들 수 있는 helper class

Form과 똑같은 방식으로 View 함수에서 사용

```python
from django import forms
from .models import Article

class ArticleForm(forms.ModelForm):

    class Meta:
        model = Article
        # 어떤 모델을 기반으로 할지 (호출하지 않는다) 등록을 하지 않는다 참조값으로 활용
        fields = '__all__'
        # 어떤 모델필드 중 어떤 것을 출력할지 결정
        # 리스트 혹은 튜플로 진행
        # ['title', 'content']
        # exclude = ('title',) 제외 시키고 싶을때 사용
```

- Meta data
  - 데이터를 표현하기 위한 데이터 
  - 예시 - 사진도 데이터인데 사진을 찍은 위치나 시각 렌즈 등을 표현 

- 참조 값과 반환 값
  - 함수를 호출하지 않고 함수 자체를 그대로 전달하여, 다른 함수에서 **"필요한 시점에"** 호출하는 경우

```python
def greeting():
    return '안녕하세요'

print(greeting) #<function greeting at 0x10761caf0>
print(greeting()) # 안녕하세요
```

- Article 이라는 클래스를 '호출하지 않고 (== model을 인스턴스로 만들지 않고)' 작성하는 이유는 ArticleForm이 해당 클래스를 필요한 시점에 사용하기 위해
- 더불어 이 경우에는 인스턴스가 필요한 것이 아닌, 실제 Article 모델의 참조 값을 통해 해당 클래스의 필드나 속성 등을 내부적으로 참조하기 위한 이유도 있음

#### view functions

- Form

  - 유효성 검사 도구 

  - 공격 및 데이터 손상에 대한 중요한  방어 수단

  -  개발자에게 강력한 편의를 제공

- ```python
  def create(request):
      form = ArticleForm(request.POST)
      if form.is_valid():
          # 통과 되면 True 못하면 False (검증과정이 추가) 검사가 간단함 그럴려고 form을 만듬
          form.save()
          return redirect('articles:index')
      return redirect('articles:new')
  ```

- 검사할 것을 추가할 수 있다

- is_valid() method
  - 유효성 검사를 실행하고, 테이터가 유효한지 여부를 boolean으로 반환
  - 데이터 유효성 검사를 보장하기 위한 많은 테스트에 대해 제공하여 개발자의 편의를 도움
- save() method
  - 하위 클래스는 키워드 인자 instance 여부를 통해 생성할 지, 수정할지를 결정함 
    - 제공되지 않은 경우 save()는 지정된 모델의 새 인스턴스를 만듦(CREATE)
    - 제공되면 save()는 해당 인스턴스를 수정 (UPDATE)
- 입력과 공백은 다르다
  - 공백은 input 태그에 required 때문에 뜬다
  - 입력은 Django가 에러메시지를 준다
- 에러메시지가 모두 다 다르다 
  - 유효성 검사로 걸러지는게 모두 다 다르기 때문에 

- form을 써서 얻는 것도 많지만 잃은 것도 있다.
  - 잃은 것 - 자율성이 떨어진다

### HTTP requests

- new-create, edit- update의  view  함수 역할을 잘 살펴보면 하나의 공통점과 차이점이 있음
  - 공통점 : 로직을 구현하기 위한 공통 목적
  - 차이점 : new와 edit는 GET 요청에 대한 처리만을 create와 update는 POST 요청에 대한 처리만을 진행

- POST를 먼저 보는 이유 
  - else: 일 때를 생각해 보라  POST가 아니라면 DB조작을 안한다
  - POST일 때만 DB을 조작하려고 한다

### View decorators

#### 데코레이터 

- 함수에 기능을 추가하고 싶을 때, 해당 함수를 수정하지 않고 기능을 추가해주는 함수 

##### HTTP methods

- 일치하지 않는 메서드 요청이라면 405 Method Not Allowed를 반환
  - 요청방법이 서버에게 전달 되었으나 사용 불가능한 상태 4 - 클라이언트(나) 5 - 서버
- 메서드 목록
  1.  require_http_methods() - 여러개 메서드를 받을 수 있다
  2.  requir_POST() - POST인 메서드만 받을 수 있다
  3.  require_safe() - GET인 메서드만 받을 수 있다



### Form 의 요점 

- 유효성 검사 도구 

- 공격 및 데이터 손상에 대한 중요한  방어 수단

-  개발자에게 강력한 편의를 제공



## authentication system

### Authentication(인증)

- 신원확인
- 사용자가 자신이 누구인지 확인하는 것

### Authorization (권한, 허가)

- 권한 부여
- 인증된 사용자가 수행할 수 있는 작업을 결정

#### 사용자

- admin

- staff

- 일반

acoounts - 회원 인증

```python
python manage.py startapp accounts 

다른 이름으로 설정해도 되지만 나중에 추가할 수 있는 생기기 때문에 accounts라고 설정한다
```

substituting a custom User model