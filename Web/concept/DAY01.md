# DAY01

## Web

경험이 중요 -최대한 많은 경험을 해봐라

시각적으로 중요 하다.

### HTML

Hyper Text markup Language

웹페이지를 작성(구조화)하기 위한 언어

.html - HTML 파일

#### 웹사이트의 구성요소

- 웹 페이지들의 모음
- 웹 페이지는 글, 그림, 동영상 등 여러가지 정보를 담고 있으며, 마우스로 클릭하면 다른 웹 페이지로 이동하는 '링크' 들이 있음. 링크를 통해 여러 웹 페이지를 연결한 것을 웹 사이트라고 함

HTML - 구조 (콘크리트)

CSS - 표현 (인테리어)

Javascript - 동작 (엘레베이터)



- 웹 사이트는 브라우저를 통해 동작함

- 브라우저마다 동작이 약간씩 달라서 문제가 생기는 경우가 많음(파편화)
- 해결책으로 웹 표준(USB)이 등장



Hyper Text 이론 (팀베너스리)

- 참조를 통해 사용자가 한 문서에서 다른 문서로 즉시 접근할 수 있는 텍스트

Markup Language

- 태그 등을 이용하여 문서나 데이터의 구조를 명시하는 언어

#### 스타일 가이드

마크업 스타일 가이드 (2 space)

기본 구조 

- html 문서의 최상위 요소

- head 문서 메타데이터 요소
  - 문서 제목, 인코딩, 스타일, 외부 파일 로딩 등
  - 일반적으로 브라우저에 나타나지 않는 내용
- body : 문서 본문 요소
  - 실제 화면 구성과 관련된 내용



#### 요소 

(여는/시작)태그 내용 (닫는/종료)태그

- 시작 태그와 종료 태그 그리고 태그 사이에 위치한 내용으로 구성

  - 요소는 태그로 컨텐츠(내용)를 감싸는 것으로 그 정보의 성격과 의미를 정의 

  - 내용이 없는 태그들도 존재
    - br, hr, img, input, link, meta

- 요소는 중첩 될 수 있음

  - 여는 태그와 닫는 태그의 쌍을 잘 확인해야함
    - 오류를 반환하는 것이 아닌 그냥 레이아웃이 깨진 상태로 출력되기 때문에, 디버깅이 힘들어 질 수 있음

  

개발자 도구를 사용해서 원하는 요소를 선택할수 있음



#### 속성

태그 속성명 속성값 태그

- 속성 지정 스타일 가이드 공백은 NO, ""(쌍따옴표) 사용

- 속성을 통해 태그의 부가적인 정보를 설정할 수 있음
- 요소는 속성을 가질 수 있으며, 경로나 크기와 같은 추가적인 정보를 제공
- 요소의 시작 태그에 작성하며 보통 이름과 값이 하나의 쌍으로 존재 
- 태그와 상관없이 사용 가능한 속성들도 있음

#### Global Attribute

id : 문서 전체에서 유일한 고유 식별자 지정



#### 시맨틱 태그

HTML 태그가 특정 목적, 역할 및 의미적 가치를 가지는 것 EX)널디

- hi 태그는 최상위 제목

구글 뉴스 상단의 메뉴는 Header 태그를 통해서 명확하게 표현하고 있음

의미론적 마크업

- 검색엔진 등에 의미 있는 정보의 그룹을 태그로 표현
- 검색 엔진 최적화를 위해서 메타태그, 시멘틱 태그 등을 통한 마크업을 효과적으로 활용 해야함

렌더링(Rendering)

- 웹 사이트 코드를 사용자가 보게 되는 웹 사이트로 바꾸는 과정

DOM 트리

- 텍스트 파일인 HTML 문서를 브라우저에서 렌더링 하기 위한 구조
  - HTML 문서에 대한 모델을 구성함
  - HTML 문서 내의 각 요소에 접근/ 수정에 필요한 프로퍼티와 메서드를 제공함



HTML 문서 구조화

- 인라인 / 블록 요소
  - 인라인 - 글자처럼 취급 / 블록 요소 - 한 줄 모두 사용

- 텍스트 요소

| 태그                      | 설명                                                         |
| :------------------------ | ------------------------------------------------------------ |
| <a></a>                   | href 속성을 활용하여 다른 URL로 연결하는 하이퍼링크 생성     |
| <b></b> <strong></strong> | 굵은 글씨 요소, 중요한 강조하고자 하는 요소 (보통 긁은 글씨로 표현) |
| <i></i><em></em>          | 기울임 글씨 요소, 중요한 강족하고자 하는 요소 (보통 기울임 글씨로 표현) |
| <br>                      | 텍스트 내에 줄 바꿈 생성                                     |
| <img>                     | src 속성을 활용하여 이미지 표현                              |
| <span></span>             | 의미 없는 인라인 컨테이너                                    |

- 그룹 컨텐츠

| 태그                      | 설명                                                         |
| :------------------------ | ------------------------------------------------------------ |
| <p></p>                   | 하나의 문단( paragraph)                                      |
| <hr>                      | 문단 레벨 요소에서의 주제의 분리를 의미하며 수평선으로 표현됨(A Horizontal Rule) |
| <ol></ol><br /><ul></ul>  | 순서가 있는 리스트(ordered)<br />순서가 없는 리스트(unordered) |
| <pre></pre>               | HTML에  작성한 내용을 그대로 표현, 보통 고정폭 글꼴이 사용되고 공백문자를 유지 |
| <blockquote></blockquote> | 텍스트가 긴 인용문 <br />주로 들여쓰기를 한것으로 표현       |
| <div></div>               | 의미 없는 블록 레벨 컨테이너                                 |



#### form

정보를 서버에 제출하기 위해 사용하는 태그 데이터를 보내기 위해 사용

ex) 로그인 ID ,PW , 게시판 작성 

기본 속성

- action : form 을 처리할 서버의 URL (데이터를 보낼곳)
- method : form을 제출할 때 사용할 HTTP 메서드(GET, POST)
- enctype : method가 post인 경우 데이터의 유형



##### input

파이썬의 input과 비슷 

- <input> id 속성 - 태그 스페셜 별명
- <label> 태그로 for 속성을 활용하여 상호 연관을 시킴

- 유형
  - text : 텍스트 입력
  - password : 입력 시 값이 보이지 않고 문자를 특수기호(*)로 표현
  - email : 이메일 형식이 아닌 경우 form 제출 불가
  - number : min, max, step 속성을 활용하여 숫자 범위 설정 가능
  - file: accept 속성을 활용하여 파일 타입 지정 가능
  - checkbox : 다중 선택
  - radio : 단일 선택
  - color : color picker
  - date : date picker
  - hidden : 사용자에게 보이지 않는 input

--------------------

### CSS

Cascading style sheets

계단식

스타일을 지정하기 위한 언어 

선택하고, 스타일을 지정한다.

선택자를 통해 스타일을 지정할 HTML 요소를 선택

- 정의 방법 
  - 인라인
    - 태그에다가 스타일을 바로 넣어 사용
  - 내부 참조 - style
  - 외부 참조 - 분리된 CSS 파일

#### 선택자의 유형

- 기본 선책자
  - 전체 선택자, 요소 선택자
  - 클래스 선택자, 아이디 선택자, 속성 선택자
- 결합자
  - 자손 결합자, 자식 결합자    - 여기까지만 해도 80%해결가능
  - 일반 형체 결합자, 인접 형제 결합자
- 의사 클래스 /요소
  - 링크, 동적 의사 클래스
  - 구조적 의사 클래스, 기타 의사 클래스, 의사 엘리먼트, 속성 선택자



#은 id

. 은 class

#### CSS 선택자 정리

- 요소 선택자
  - HTML 태그를 직접 선택
- 클래스 선택자
  - 마침표(.)문자로 시작하며, 해당 클래스가 적용된 항목을 선택
- 아이디(id) 선택자
  - #문자로 시작하며, 해당 아이디가 적용된 항목을 선택
  - 일반적으로 하나의 문서에 1번만 사용
  - 여러 번 사용해도 동작하지만, 단일 , id를 사용하는 것을 권장

#### 적용 우선순위

**범위가 좁을수록 강하다.**

!important == 잘 안쓴다.



CSS 상속

```html
<div>
    <p>
        
    </p>
</div>
```

상속 되는 것 예시

Text 관련 요소

상속되지 않는 것 예시

여백X, 레이아웃X

#### 크기단위

- 픽셀
  - 모니터 해상동의 한 화소인 ' 픽셀'기준
  - 픽셀의 크기는 변하지 않기 때문에 고정적인 단위
  - 화면 (핸드폰, 노트북)
- %
  - 백분율 단위
  - 가변적인 레이아웃에서 자주 사용
- em
  - 부모 태그 자식 태그 (위 부모 태그에 비례해서 영향을 받음)
- rem
  - 상속의 영향을 받지 않음
  - 최상위 요소의 사이즈를 기준으로 배수 단위를 가짐

box model

content padding, margin, border

#### display

display에 따라 크기와 배치가 달라진다.

display : block

- 줄 바꿈이 일어나는 요소
- margin이 블록 차지

display : inline   - 글자처럼 취급

- content 너비만큼 가로 폭을 차지한다. (내용물)
- width, height, margin-top, margin-bottom을 지정할 수 없다.
- 상하 여백은 line- height로 지정한다.
- 기본 너비는 컨텐츠 영역만큼

블록 레벨 요소와 인라인 레벨 요소

#### position

1. relative : 상대 위치
   - 자기 자신의 static위치를 기준으로 이동
2. absolute : 절대 위치
   - 


