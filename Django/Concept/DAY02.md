# DAY02

#### namespace

페이지가 많아지면 똑같은 이름의 페이지가 있을때 첫번째 페이지에서만 잇음

하이퍼 링크를 눌러도 현재페이지에만 있음

주소를 직접 넣어줘도 현재페이지에만 있음

```ptyhon
urls.py
app_name = 'articles'

.html
<a href={% url 'articles:throw' %}>
```

이렇게 해도 두번째 페이지로 움직이지 않는다.

#### templates namesapce

templates 안에 app과 똑같은 이름의 파일을 넣어준다

```python
views.py
return render(request, 'articles/index.html')

return render(request, 'pages/index.html')
```

여기까지 해준다면 다음 페이지로 넘어간다.

#### Database

##### 스키마 

- 뼈대 

- 데이터베이스에서 자료의 구조, 표현 방법, 관계 등을 정의한 구조

##### 테이블 

- 필드와 레코드를 사용해 조직되 데이터 요소들의 집합
- 관계라고도 부름
- 필드 
  - 속성, 컬럼
  - 각 필드에는 고유한 데이터 형식이 지정됨 (INT, TEXT)
- 레코드 
  - 튜플, 행
  - 테이블의 데이터는 레코드에 저장됨
- pk 
  - 기본키 (ID)
  - 각 레코드의 고유한 값(식발자로 사용)
  - 기술적으로 다른 항목과 절대로 중복되어 나타날 수 없는 단일 값
  - 주민등록번호 
- 퀴리(Query)
  - 데이터를 조회하기 위한 명령어를 일컬음
  - 조건에 맞는 데이터를 추출하거나 조작하는 명령어 

## Model

- Django는 Model을 통해 데이터에 접속하고 관리

- 단일한 데이터에 대한 정보를 가짐

- 저장된 데이터 베이스의 구조

- 일반적으로 각각의 모델은 하나의 데이터 베이스 테이블에 매핑( 하나의 값을 다른 값으로 대응시키는 것)
  - 모델 클래스 1개 == 데이터베이스 테이블 1개 

- 각 모델은 django.models.Modle 클래스의 서브 클래스로 표현됨
  - 즉, 각 모델은 django.db.models 모듈의 Model 클래스를 상속받아 구성됨
  - 클래스 상속 기반 형태의 Django 프레임워크 개발

- 필드 - 컬럼 

- 동작들  - oop(메서드)

- 데이터 베이스는 아니다.

- 클래스 상속 기반 형태의 Django 프레임워크 개발 

- models 모듈을 통해 어떠한 타입의 DB필드(컬럼)을 정의할 것인지 정의 

- 클래스 변수 title과 content는 DB필드를 나타냄

- **공식문서**를 잘 찾아 봐야 된다.
  - 목차를 먼저 봐라 
  - 다 이해하려고 하지마라 

```ptyhon
class Article(models.Model):
    title = models.CharField(max_length=10) 
    # 제목의 길이를 최대 10자 까지 가능하다.
    content = models.TextField()
    # 내용은 글자수 제한 없이 사용가능
```

- CharField(max_length=None)
  - 길이의 제한이 있는 문자열을 넣을 때 사용 
  - max_length
    - 필드의 최대 길이 = 255
    - CharField의 필수 인자
    - 데이터베이스와 Django의 유효성 검사에서 활용됨
- TextField(**options)
  - 글자의 수가 많을 때 사용
  - max_length 옵션 작성 시 사용자 입력 단계에서 반영되지만, 모델과 데이터베이스 단계에는 적용되지 않음 (CharField를 사용해야 함)
    - 실제로 저장될 때 길이에 대한 유효성을 검증하지 않음
  - 2**31 -1 SQLite

  ### Migrations

1. makemigrations

   - 모델을 작성 혹은 변경한 것에 기반한 새로운 migration(설계도)을 만들 때 사용
   - migrations/0001_initial 생성

   ```python
   python manage.py makemigrations
   ```

2. migrate

   - makemigrations로 만든 설계도를 실제 db.sqlite3 DB파일에 반영하는 과정
   - 결과적으로 모델에서의 변경사항들과 DB의 스키마가 동기화를 이룸
     - 모델과 DB의 동기화
   - 기존에 있던 것도 설계도를 가지고 있어 처음에 할 때 많이 나온다.
   
   ```python
   python manage.py migrate
   ```

데이터 베이스를 읽으려면 sqlite 를 설치해줘야된다.

**중요**

model.py 변경사항이 생기면

migration 생성

migrate 반영

설계도가 늘어나는게 커밋 이랑 비슷한거 



#### ORM

- 객체 지향 맵핑 

- 객체 지향 프로그래밍 언어를 사용하여 호환되지 않는 유형의 시스템 간에 데이터를 변환하는 프로그래밍 기술 

- 객체 지향 프로그래밍에서 데이터베이스을 연동할 때, 데이터베이스와 객체 지향 프로그래밍 언어 간의 호환되지 않는 데이터를 변환하는 프로그램이 기법

- Django ORM 사용

- 장점

  - SQL을 잘 알지 못해도 객체지향 언어로 DB조작이 가능 

  - 객체 지향적 접근으로 인한 높은 생산성

- 단점(교육을 들을 때는 괜찮다)
  - ORM 만으로 완전한 서비스를 구현하기 어려운 경우가 있음

- 쓰는이유

  - 생산성

  - DB를 객체로 조작하기 위해 ORM을 사용할 것

##### DatatimeField

1. auto_now_add
   - 최초 생성 일자(표준시로 작성 - 'ko-kr'로 시간이 자동으로 바꿈)
   - 최초 insert시에만 현재 날짜와 시간으로 갱신 
2. auto_now
   - 최종 수정 일자 
   - save를 할 때마다 현재 날짜와 시간으로 갱신 

- 정리 - 웹 애플리케이션의 데이터를 구조화하고 조작하기 위한 도구

#### QureySet API

##### Database API

- Django가 기본적으로 ORM을 제공함에 따른 것으로 DB를 편하게 조작할 수 있도록 도움

- Model을 만들면 Django는 객체들을 만들고 읽고 수정하고 지울 수 있는 DB API를 자동으로 만듬

##### 'objects' manager

- 기본적으로 모든 Django 모델 클래스에 대해 objects라는 manager 객체를 자동으로 추가함

- 특정 데이터를 조작 할 수 있음

- DB를 Python class로 조작할 수 있도록 여러 메서드를 제공하는  manager

##### Qurey

- 데이터베이스에 특정한 데이터를 보여달라는 요청

##### QuerySet 

- 데이터 베이스에게서 전달 받은 객체 목록
  - 순회가 가능한 데이터로써 1개 이상의 데이터를 불러와 사용할 수 있음 인덱스로도 접근할수 있음
- ORM 을 통해 만들어진 자료형, 필터를 걸거나 정렬 등을 수행할 수 있음
- 'objects' manager를 사용하여 복수의 데이터를 가져오는 qureyset method를 사용할 때 반환되는 객체
- 데이터베이스가 단일한 객체를 반환 할 때 QuerySet이 아닌 모델의 인스턴스로 반환됨
- 생성하고 읽고 수정하기 

### CRUD

- Create / Read/ Update/ Delete
  - 생성/ 조회/ 수정/ 삭제

#### Create

데이터 객체를 만드는(생성하는) 3가지 방법 

1. ```python
   article.title = 'first'
   
   article.content = 'django!'
   
   article.save()
   ```

   1. article = Article()

   - 클래스를 통한 인스턴스 생성

   2. article.title

   - 클래스 변수명과 같은 이름의 인스턴스 변수를 생성 후 값 할당

   - article.content

   3. article.save()

   - 인스턴스로 save 메서드 호출

2. ```python
   article = Article(title='second', content='django!')   
   
   article.save()
   #저장을 꼭 해줘야 한다
   ```

3. ```python
   Article.objects.create(title='third', content='django!')
   #save를 안해줘도 자동으로 해준다
   ```

```sqlite
# 결과값
1	first	django!	2022-08-31 05:43:53.624813	2022-08-31 05:51:05.769993
2	second	django!	2022-08-31 05:52:25.295830	2022-08-31 05:52:25.295830
3	third	django!	2022-08-31 05:54:52.533561	2022-08-31 05:54:52.533561
```

#### READ

- 제일 중요하다
- Methods that "return new querysets" - 목록을 받는가?
- Methods that "do not return querysets" - 단일 목록을 받는가?

##### all()

- 전체 데이터 조회

##### get()

- 단일 데이터 조회

- 둘 이상의 객체를 찾으면 MultipleObjectsReturned 예외를 발생시킴

- 고유성을 보장한는 조회에서 사용해야 함 (id =1, pk=1)

- pk 는 무조건 get에서만 사용

##### filter()

- 지정된 조회 매개 변수와 일치하는 객체를 포함하는 새 Queryset을 반환

**주의 사항**

- 없어도 빈 [] QuerySet으로 반환

- 하나만 이어도 QuerySet으로 반환

- pk = 1이걸로 주면 QuerySet으로 줘서 두번 들어가야됨

- pk= 1이 없으면 빈 [] QuerySet으로 반환해서 안됨

##### Field lookups 

- 특정 레코드에 대한 조건을 설정하는 방법

- '_ _' 두개를 써서 사용  

#### Updata

- 수정하고자 하는 객체를 조회를 하고 변수에 저장

- 변수에 새로운값 할당
- save() 를 꼭해줘야 DB에서 변화한다

```python
In [29]: article = Article.objects.get(pk=1)

In [30]: article
Out[30]: <Article: Article object (1)>

In [31]: article.title = 'byebye'

In [32]: article.save()
```



#### Delete

- 삭제하고자 하는 article 인스턴스 객체를 조회 후 반환 값을 저장
- 삭제되면 재사용을 안함. 필요없다고 생각을 하기 때문에 1 번을 삭제하고 다시 넣어주면 id는 4으로 할당

```python
In [29]: article = Article.objects.get(pk=1)

In [33]: article.delete()
Out[33]: (1, {'articles.Article': 1})
```



GET = 조회

POST = 조작