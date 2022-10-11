# DAY06

### 정적 파일

- 파일 자체가 고정되어 있고, 서비스 중에도 추가되거나 변경되지 않고 고정 되어있음
  - 웹 사이트는 일반적으로 이미지, 자바 스크립트 또는 CSS와 같은 미리 준비된 추가 파일(움직이지 않는)을 제공해야 함
- Django에서는 이러한 파일들을 "static file" 이라 하고, staticfiles 앱은 설치 되어 있음(내장 앱)

### Media File

- 사용자가 웹에서 업로드하는 정적 파일(user-uploaded)

### 정적 파일을 구성하고 사용하기 위한 몇 가지 단계

```python
# 첫번째
INSTALLED_APPS = [
'django.contrib.staticfiles',
]
# 이미 설치되어있음
# 두번째
STATIC_URL = '/static/'

# 세번째
앱의 static 폴더에 정적 파일을 위치하기

# 네번째
템플릿에서 static 템플릿 태그를 사용하여 지정된 경로에 있는 정적파일을 URL로 만들기
```

````django
{% load %}
load tag
특정 라이브러리, 패키지에 등록된 모든 템플릿 태그와 필터를 로드

{% static '' %}
static tag
STATIC_ROOT에 저장된 정적 파일에 연결
````

1. STATIC_ROOT
   - collectstatic이 배포를 위해 정적 파일을 수집하는 디렉토리의 절대 경로
   - 개발 과정에서 setting.py DEBUG 값이 True 로 설정되어 있으면 해당 값은 작용되지 않음
   - 실 서비스 환경에서 Django의 모든 정적 파일을 다른 웹 서버가 직접 제공하기 위해 사용
   - 배포 환경에서는 Django 를 직접 실행하는 것이 아니라, 다른 서버에 의해 실행되기 때문에 실행하는 다른 서버는 Django에 내장되어 있는 정적 파일들을 인식하지 못함
2. STATICFILES_DIRS
   - app/static/ 디렉토리 경로를 사용하는 것 외에 추가적인 정적 파일 경로 목록을 정의하는 리스트
   - 추가 파일 디렉토리에 대한 전체 경로를 포함하는 문자열 목록으로 작성되어야 함
3. STATIC_URL
   - STATIC_ROOT에 있는 정적 파일을 참조할 때 사용할 URL
   - 개발 단계에서는 실제 정적 파일들이 저장되어 있는 app/static/ 경로 및 STATICFLES_DIRS 에 정의된 추가 경로들을 탐색
   - 실제 파일이나 디렉토리가 아니며, URL로만 존재
   - 비어 있지 않은 값으로 설정 한다면 반드시 slash(/)로 끝나야 함

### ImageField()

- 이미지 업로드에 사용하는 모델 필드
- FileField를 상속받는 서브 클래스이기 때문에 FileField의 모든 속성 및 메서드를 사용 가능
- 더해서 사용자에 의해 업로드 된 객체가 유효한 이미지인지 검사
- ImageField 인스턴스는 최대 길이 100자인 문자열로 DB에 생성되며, max_length 인자를 사용하여 최대 길이를 변경 할 수 있음

### FileField()

- 선택인자
  - upload_to= '경로' 
  - storage

- setting. py MEDIA_ROOT, MEDIA_URL 설정
- upload_to 속성을 정의하여 업로드 된 파일에 사용할 MEDIA_ROOT의 하위 경로를 지정(선택사항)

1. MEDIA_ROOT
   - 사용자가 업로드 한 파일들을 보관할 디렉토리의 절대 경로
   - Django는 성능을 위해 업로드 파일은 데이터 베이스에 저장하지 않음
     - 데이터베이스에 저장되는 것은 '파일 경로'
   - MEDIA_ROOT는 STATIC_ROOT와 반드시 다른 경로로 지정해야 함
2. MEDIA_URL
   - MEDIA_ROOT에서 제공되는 미디어 파일을 처리하는 URL
   - 업로드 된 파일을 주소(URL)를 만들어 주는 역할
     - 웹 서버 사용자가 사용하는 public URL
   - 비어 있지 않은 값으로 설정 한다면 반드시 slash(/)로 끝나야 함
   - MEDIA_URL은 STATIC_URL과 반드시 다른 경로로 지정해야 함

