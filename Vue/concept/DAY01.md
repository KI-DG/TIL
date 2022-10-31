# DAY01

### Web App

- 웹 브라우저에서 실행되는 어플리케이션 소프트웨어
- 개발자 > 디바이스 모드 
- 웹 페이지가 그대로 보이는 것이 아닌 디바이스에 설치된 App처럼 보이는 것
- 웹 페이지가 디바이스에 맞는 적절한 UX/UI로 표현되는 형태

### SPA

- 서버에서 최초 1장의 HTML만 전달받아 모든 요청에 대응하는 방식
  - CSR(Client side Rendering) 방식으로 요청을 처리하기 때문

### CSR

- 최초 한 장의 HTML을 받아오는 것은 동일
  - server로 부터 최초로 받아오는 문서는  빈 html 문서
- JS를 사용하여 필요한 부분만 다시 렌더링
  1. 필요한 페이지를 서버에 AJAX로 요청
  2. 서버는 화면을 그리기 위해 필요한 데이터를 JSON 방식으로 전달
  3. JSON 데이터를 JS처리 DOM 트리에 반영(렌더링)
- 장점
  1. 모든 HTML 페이지를 서버로부터 받는 것이 아니기 때문
     - 클라이언트 - 서버간 통신 즉, 트래픽 감소
     - 트래픽이 감소한다 == 응답 속도가 빨라진다
  2. 매번 새 문서를 받아 새로고침하는 것이 아니라 필요한 부분만 고쳐 나가므로 각 요청이 끊김없이 진행
     - SNS에서 추천을 누를 때 마다 첫 페이지로 돌아간다 = 끔직한 App
     - 요청이 자연스럽게 진행이 된다 = UX 향상
  3. BE와 FE의 작업 영역을 명확히 분리 할 수 있음
     - 각자 맡은 역할을 명확히 분리한다 = 협업이 용이해짐

- 단점
  - 첫 구동 시 필요한 데이터가 많을수록 최초 작동 시작까지 오랜 시간이 소요
  - 잠깐의 로딩 시간이 필요
  - 검색 엔진 최적화가 어려움
    - 서버가 제공하는 것은 텅 빈 HTML
    - 내용을 채우는 것은 AJAX 요청으로 얻은 JSON 데이터로 클라이언트가 진행
  - 대체적으로 HTML에 작성된 내용을 기반으로 하는 검색엔진에 빈 HTML을 공유하는 SPA 서비스가 노출되기는 어려움
- CSR vs SSR
  -  흑과 백이 아님
    - 내 서비스에 적합한 렌더링 방식을 적절하게 활용할 수 있어야 함
  - SPA 서비스에서도 SSR을 지원하는 Framework도 발전하고 있음

## Vue

- CDN
  - Vue로 작업을 시작하기 위하여 CDN을 가져와야 함
  - Django == Python Web Framework
    - pip install
  - Vue === JS Front-end Framework
    - Bootstrap에서 사용하였던 CDN 방식 제공

- 코드 작성하기 

  1. Vue CDN 가져오기

  ````html
  <script src="https://cdn.jsdelivr.net/npm/vue@2.7.13/dist/vue.js"></script>
  ````

  2. Vue instance생성
  3. el, data 설정
     - data에 관리할 속성 정의
  4. 선언적 렌더링 {{}}
     - Vue data를 화면에 렌더링
  5. input tag에 v-model 작성

- MVVM Pattern
  - 소프트웨어 아키텍처 패턴의 일종
  - 마크업 언어로 구현하는 그래픽 사용자 인터페이스(view)의 개발을 Back-end(model)로 부터 분리시켜 view가 어느 특정한 모델 플랫폼에 종속되지 않도록 함
  - View - 우리 눈에 보이는 부분 = DOM
  - Model - 실제 데이터 = JSON
  - View Model(Vue)
    - View를 위한 Model
    - View와 연결(binding)되어 Action을 주고 받음
    - Model이 변경되면 View Model도 변경되고 바인딩된 View도 변경됨
    - View에서 사용자가 데이터를 변경하면 View Model의 데이터가 변경되고 바인딩된 다른 View도 변경됨
  - MVC 패턴에서 Contrtoller를 제외하고 View Model을 넣은 패턴
  - View는 Model을 모르고 Model도 View를 모름 (독립성 증가, 적은 의존성)
    - DOM은 Data 모르고, Data도 DOM을 모름 (직접적으로 연결되어 있지 않다)
  - View에서 데이터를 변경하면 View Model의 데이터가 변경되고, 연관된 다른 View도 함께 변경된다

- Vue instance
  - 1개의객체
  - 아주 많은 속성과 메서드를 이미 가지고 있고, 이러한 기능들을 사용하는 것

- 생성자 함수 
  - 동일한 구조의 객체를 여러 개 만들고 싶으면 사용
  - 생성자 함수는 특별한 함수를 의미하는 것이 아님
  - new 연산자로 사용하는 함수 
  - 함수 이름은 반드시 대문자로 시작

- el (element)
  - Vue instance 와 DOM 을 mount(연결)하는 옵션
    - View와 Model을 연결하는 역할
    - HTML id 혹은 class와 마운트 가능
  - Vue instance와 연결되지 않은 DOM 외부는 Vue의 영향을 받지 않음
    - Vue 속성 및 메서드 사용 불가

- data 

  - Vue instance의 데이터 객체 혹은 인스턴스 속성
  - 데이터 객체는 반드시 기본 객체 {} 여야 함
  - 객체 내부의 아이템들은 value로 모든 타입의 객체를 가질 수 있음
  - 정의된 속성은 interpolation {{}} 을 통해 view에 렌더링 가능함

- methods

  - Vue instance의 method들을 정의하는 곳
  - 객체 정의
    - 객체 내 print method 정의
    - print method 실행 시 Vue instance의 data내 message 출력
  - method를 호출하여 data 변경 가능
    - 객체 내 bye method 정의

  - 콘솔창에서 app.bye() 실행
    - DOM에 바로 변경된 결과반영

- methods with Arrow Function 
  - 메서드를 정의 할 때 Arrow Function 을 사용하면 안됨
  - Arrow Function의 this는 함수가 선언될 때 상위 스코프를 가르킴
  - this가 상위 객체 window를 가리킴
  - 호출은 문제 없이 가능하나 this로 Vue의 data를 변경하지 못함
  - 콜백 함수 안에서는 써도 된다

### Template Syntax

- 렌더링 된 DOM을 기본 Vue instance의 data에 선언적으로 바인딩 할 수 있는 HTML 기반 template syntax를 사용
  - 렌더링 된 DOM - 브라우저에 의해 보기 좋게 그려질 HTML 코드
  - HTML 기반 template syntax - HTML 코드에 직접 작성할 수 있는 문법 제공
  - 선언적으로 바인딩 - Vue instance와 DOM을 연결

- Template Interpolation
  - 가장 기본적인 바인딩(연결) 방법
  - 중괄호 2개로 표기
  - DTL과 동일한 형태로 작성
  - HTML을 일반 텍스트로 표현
- RAW HTML
  - v-html directive을 사용하여 data와 바인딩
  - directive - HTML 기반 template syntax
  - HTML의 기본 속성이 아닌 Vue가 제공하는 특수 속성의 값으로 data를 작성

### Directives

- v-접두사가 있는 특수 속성에는 값을 할당 할 수 있음
  - 값에는 JS 표현식을 작성 할 수 있음
- directive의 역할은 표현식의 값이 변경될 때 반응적으로 DOM에 적용하는 것
- `:` 을 통해 전달 인자를 받을 수 있음
- `.` 으로 표시되는 특수 접미사 - directive를 특별한 방법으로 바인딩 해야 함

````html
v-on:submit.prevent="onSubmit"
이벤트 취소랑 비슷

````

#### v-text

- `{{}}` 와 동일한 역할

#### v-html

- RAW HTML 을 표현할 수 있는 방법
- 사용자가 입력하거나 제공하는 컨텐츠에는 절대 사용 금지

####  v-show

- 표현식에 작성된 값에 따라 element를 보여 줄 것인지 결정
  - boolena값이 변경될 때 마다 반응
- 대상 element의 display 속성을 기본 속성과 none으로 toggle
- 요소 자체는 항상 DOM에 렌더링 됨
- 바인딩 된 isActive의 값이 false이면 첫 방문시 보이지 않음
- 화면에서만 사라졌을 뿐, DOM에는 존재함

#### v-if

- v-how와 사용 방법은 동일
- isActive 의 값이 변경 될 때 반응
- 값이 false인 경우 DOM에서 사라짐

#### v-show VS v-if

- v-show 
  - 초기 렌더링에 필요한 비용은 높지만 바꾸는 비용은 싸다 
- v-if 
  - 초기 비용은 적으나 표현식 값이 자주 변경되는 경우 잦은 재 렌더링으로 비용이 증가할 수 있음

#### v-for 

- for .. in .. 형식으로 작성 
- 반복한 데이터 타입에 모두 사용 가능
- index를 함께 출력하고자 한다면 (char, index) 형태로 사용 가능
- 배열 역시 문자열과 동일하게 사용 가능
- 특수 속성 key
  - v-for 사용 시 반드시 key 속성을 각 요소에 작성
  - 주로 v-for directive 작성 시 사용
  - vue 화면 구성 시 이전과 달라진 점을 확인 하는 용도로 활용
    - 따라서 key가 중복되어서는 안됨
  - 각 요소가 고유한 값을 가지고 있지 않다면 생략할 수 있음
- 객체 순회 시 value가 할당되어 출력
- 2번째 변수 할당시 key 출력가능

#### v-on

- `:` 을 통해 전달받은 인자를 확인
- 값으로 JS 표현식 작성
- addEventListener의 첫 번째 인자와 동일한 값들로 구성
- 대기하고 있던 이벤트가 발생하면 할당된 표현식 실행
- method를 통한 data 조작도 가능
- method에 인자를 넘기는 방법은 일반 함수를 호출할 때와 동일한 방식
- `:`을 통해 전달된 인자에 따라 특별한 modifiers(수식어) 가 있을 수 있음
- `@` shortcut 제공 (축약해서 사용가능)

#### v-bind

- HTML 기본 속성에 Vue data를 연결
- class의 경우 다양한 형태로 연결 가능
  - 조건부 바인딩
    - 삼항연산자도 가능
    - {'class Name': '조건 표현식'}
  - 다중 바인딩
    - ['JS 표현식', 'JS 표현식', ...]
- Vue data의 변화에 반응하여 DOM에 반영하므로 상황에 따라 유동적 할당 가능
- `:` shortcut 제공 (축약해서 사용가능)

#### v-model

- Vue instance와 DOM의 양방향 바인딩
- Vue data 변경 시 v-model로 연결된 사용자 입력 element에도 적용

### Vue advanced

#### computed

- Vue instace가 가진 options 중 하나
- computed 객체에 정의한 함수를 페이지가 최초로 렌더링 될 때 호출하여 계산
  - 계산 결과가 변하기 전까지 함수를 재호출하는 것이 아닌 계산된 값을 반환

#### method VS computed

- method
  - 호출 될 때마다 함수를 실행
  - 같은 결과여도 매번 새롭게 계산
- computed
  - 함수의 종속 대상의 변화에 따라 계산 여부가 결정됨
  - 종속 대상이 변하지 않으면 항상 저장(캐싱)된 값을 반환

#### watch

- 특정 데이터의 변화를 감지하는 기능 (감시자)
  1. watch 객체를 정의
  2. 감시할 대상 data를 지정
  3. data가 변할 시 실행 할 함수를 정의
- 첫번째 인자는 변동 전 data
- 두번째 인자는 변동 후 data
- 실행 함수를 Vue method로 대체 가능
  1. 감시 대상 data의 이름으로 객체 생성
  2. 실행하고자 하는 method를 handler에 문자열 형태로 할당
- Array, Object의 내부 요소 변경을 감지를 위해서는 deep 속성 추가 필요

#### filters

- 텍스트 형식화를 적용할 수 있는 필터
- interpolation 혹은 v-bind를 이용할 때 사용 가능
- 필터는 자바스크립트 표현식 마직막에 `|`(엔터키 위)와 함께 추가되어야 함
- 이어서 사용 가능