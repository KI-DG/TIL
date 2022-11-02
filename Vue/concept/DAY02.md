# DAY02

### Node.js

- 자바스크립트는 브라우저를 조자가는 유일한 언어
  - 하지만 브라우저 밖에서는 구동할 수 없었음
- 자바스크립트를 구동하기 위한 런타임 환경인 Node.js 로 인해 브라우저가 아닌 환경에서도 구동할 수 있게 됨

- NPM (Node package Manage)
  - python 에 pip == Node.js 는 npm
  - 다양한 의존성 패키지를 관리
- Node.js 설치 시 함께 설치 됨

### Vue CLI

- Vue 개발을 위한 표준 도구
- 프로젝트의 구성을 도와주는 역할
- 확장 플러그인, GUI, Babel등 다양한 tool 제공
- git init이 되어있는 상태

```bash
설치 어디에서든지 git bash를 켜서 만들수 있음
$ npm install -g @vue/cli

프로젝트 생성 
vscode terminal에서 진행
$ vue create vue-cli

Vue 버전 선택(Vue 2)

출력된 명령어 실행
프로젝트 디렉토리로 이동
$ cd vue-cli

프로젝트 실행
$ npm run serve
```



#### node_modules

- node.js 환경의 여러 의존성 모듈
- python의 venv 와 비슷한 역할을 함
  - .gitignore에 넣어준다
  -  Vue 프로젝트를 생성하면 자동으로 추가됨

#### Babel

- 자바스크립트의 ES6+ 코드를 구버전으로 번역/변환 해주는 도구
- 자바스크립트의 파편화, 표준화의 영향으로 작성된 코드의 스펙트럼이 매우 다양

#### Webpack

- static module bundler
- 모듈 간의 의존성 문제를 해결하기 위한 도구
- 프로젝트에 필요한 모든 모듈을 매핑하고 내부적으로 종속성 그래프 빌드함

#### Module

- 개발하는 애플리케이션 크기가 커지고 복잡해지면 파일 하나에 모든 기능을 담기가 어려워짐
- 자연스럽게 파일을 여러 개로 분리하여 관리를 하게 되었고, 이때 분리된 파일 각각이 모듈 즉, js 파일 하나가 하나의 모듈 

- 모듈은 대개 기능 단위로 분리하며, 클래스 하나 혹은 특정한 목적을 가진 복수의 함수로 구성된 라이브러리 하나로 구성됨
- 여러 모듈 시스템
  - ESM(ECMA Script Module), AMD, CommonJS, UMD
- Module 의존성 문제
  - 모듈의 수가 많아지고 라이브러리 혹은 모듈 간의 의존성(연결성)이 깊어지면서 특정한 곳에서 발생한 문제가 어떤 모듈 간의 문제인지 파악하기 어려움
    - Webpack은 이 모듈 간의 의존성 문제를 해결하기 위해 등장

#### Bundler

- 모듈 의존성 문제를 해결해주는 작업이 Bundling
- 이러한 일을 해주는 도구가 Bundler이고, Webpack은 다양한 Bundler 중 하나
- 모듈들을 하나로 묶어주고 묶인 파일은 하나(혹은 여러 개) 로 만들어짐
- Bundling된 결과물은 개별 모듈의 실행 순서에 영향을 받지 않고 동작하게 됨
- snowpack, parcel, rollup.js 등의 webpack 이외에도 다양한 모듈 번들러 존재
- Vue CLI 는 이러한 Babel, Webpack에 대한 초기 설정이 자동으로 되어 있음

#### package.json

- 프로젝트의 종속성 목록과 지원되는 브라우저에 대한 구성 옵션을 포함

#### package-lock.json

- 수정하지 않아도 됨( 자동으로 들어감 )
- node_modules에 설치되는 모듈과 관련된 모든 의존성을 설정 및 관리
- 협업 및 배포 환경에서 정확히 동일한 종속성을 설치하도록 보장하는 표현
- 사용 할 패키지의 버전을 고정
- 개발 과정 간의 의존성 패키지 충돌 방지
- python의 requirments.txt 역할

#### public/index.html

- Vue 앱의 뼈대가 되는 html 파일
- Vue 앱과 연결될 요소가 있음

#### src

- src/assets
  - 정적 파일을 저장하는 디렉토리
- src/components
  - 하위 컴포넌트들의 위치
- src/App.vue
  - 최상위 컴포넌트
  - public/index.html과 연결됨
- src/main.js
  - webpack이 빌드를 시작할 때 가장 먼저 불러오는 entry point
  - public/index.html과 src/App.vue 를 연결시키는 작업이 이루어지는 곳
  - Vue 전역에서 활용 할 모듈을 등록할 수 있는 파일

### SFC

#### Component

- UI를 독립적이고 재사용 가능한 조각들로 나눈 것
  - 즉, 기능별로 분화한 코드 조각
- CS에서는 다시 사용할 수 있는 범용성을 위해 개발된 소프트웨어 구성 요소를 의미
- 하나의 app을 구성할 때 중첩된 컴포넌트들의 tree로 구성하는 것이 보편적임
- 컴포넌트는 유지보수를 쉽게 만들어 줄 뿐만 아니라 재사용성의 측면에서도 매우 강력한 기능을 제공
- 우리가 사용하는 웹 서비스는 여러 개의 컴포넌트로 이루어져 있음 
- 하나의 컴포넌트를 만들어두면 반복되는 UI를 쉽게 처리할 수 있음

#### SFC 

- Vue instance란 - new Vue() 로 만든 인스턴스

- 하나의 .vue 파일이 하나의 vue instance이고, 하나의 컴포넌트이다
  - single File Component
- Vue instance에서는 HTML, CSS, JavaScript 코드를 한번에 관리
  - 이 Vue instance를 기능 단위로 작성하는 것이 핵심
- 컴포넌트 기반 개발의 핵심 기능
- 기능단위로 쪼개야 된다

#### Vue component 구조

- 템플릿(HTML)
  - HTML의 body 부분
  - 눈으로 보여지는 요소 작성
  - 다른 컴포넌트를 HTML 요소처럼 추가 가능
- 스크립트(javaScript)
  - JavaScript 코드가 작성되는 곳
  - 컴포넌트 정보, 데이터, 메서드 등 vue 인스턴스를 구성하는 대부분이 작성됨
- 스타일(CSS)
  - CSS 가 작성되며 컴포넌트의 스타일 담당
- 컴포넌트들의 tree구조를 이루어 하나의 페이즈를 만듦
- root에 해당하는 최상단의 component 가 App.vue
- App.vue를 index.html과 연결
- 결국 index.html 파일 하나만을 rendering 
  - 이게 바로 SPA

#### 컴퍼넌트 만든 과정

1. 파일을 만든다
2. 이름 등록
3. 최상위 요소 추가 (반드시 하나의 요소만 추가 가능)
   - 비어 있어도 안됨
   - 해당 요소 안에 추가 요소를 작성해야 함

#### *component* 등록 3단계 (중요)

1. 불러오기
2. 등록하기
3. 보여주기

== django에서 url view html

```bash
npm install 만 하면  node_modules 가 됨
```

### Data in components

- 동적 웹페이지를 만들고 있음
- 필요한 컴포넌트들끼리 데이터를 주고받으면 될까?
  - 데이터의 흐름을 파악하기 힘듦
  - 개발 속도 저하
  - 유지보수 난이도 증가
- 컴포넌트는 부모-자식 관계를 가지고 있으므로, 부모-자식 관계만 데이터를 주고받게 하자!
  - 데이터의 흐름을 파악하기 용이
  - 유지보수 하기 쉬워짐
- 부모 - 자식로의 데이터의 흐름
  - pass props의 방식
- 자식 - 부모로의 데이터의 흐름
  - emit event 방식

#### Pass Props

- 요소의 속성을 사용하여 데이터 전달
- props는 부모(상위) 컴포넌트의 정보를 전달하기 위한 사용자 지정 특성
- 자식(하위) 컴포넌트는 props 옵션을 사용하여 수신하는 props를 명시적으로 선언해야 함

- 정적인 데이터를 전달하는 경우 static props라고 명시하기도 함
- 요소에 속성을 작성하듯이 사용 가능하여, prop-data-name="value"의 형태로 데이터를 전달
  - 이 때 속성의 키 값은 kebab-case를 사용
- 보내는 쪽과 받는 쪽의 데이터가 다르다
- 타입을 쓰는 이유 = 유효성 검사를 위해

- 부모에서 넘겨주는 props
  -  kebab-case
- 자식에서 받는 props
  - camelCase
- 각 vue 인스턴스는 같은 data 객체를 공유하므로 새로운 data 객체를 반환(return)하여 사용해야 함
- 한 단계만 내려갈 수 있음

##### 단방향 데이터 

- 모든 props는 부모에서 자식으로 즉 아래로 단방향 바인딩을 형성
- 부모 속성이 업데이트 되면 자식으로 흐리지만 반대 방향은 아님
  - 부모 컴포넌트가 업데이트될 때마다 자식 컴포넌트의 모든 prop들이 최신 값으로 새로고침 됨
- 목적 
  - 하위 컴포넌트가 실수로 상위 컴포넌트 상태를 변경하여 앱의 데이터 흐름을 이해하기 힘들게 만드는 것을 방지
- 하위 컴포넌트에서 prop를 변경하려고 시도해서는 안되며 그렇게 하면 Vue는 콘솔에서 경고로 출력함

#### Dynamic props

- 변수를 props로 전달할 수 있음
- v-bind directive를 사용해 데이터를 동적으로 바인딩
- 부모 컴포넌트의 데이터가 업데이트 되면 자식 컴포넌트로 전달되는 데이터 또한 업데이트 됨

```vue
// 문자열 '1'을 전달
<SomeComponent num-props="1"/>
// props로 숫자로써의 1을 전달
<SomeComponent :num-props="1"/
```

#### Emit Event

- 자식 컴포넌트에서 부모 컴포넌트로 데이터 전달할 때는 이벤트를 발생 시킴
- 이벤트를 발생시키는게 어떻게 데이터를 전달하는 것일까?
  - 데이터를 이벤트리스너의 콜백함수의 인자로 전달
  - 부모 컴포넌트는 해당 이벤트를 통해 데이터를 받음
- $emit
  - $emit 메서드를 통해 부모 컴포넌트에 이벤트를 발생
    - $emit('event-name') 형식으로 사용하며 부모 컴포넌트에 event-name이라는 이벤트를 발생시킴
    - 마치 사용자가 마우스 클릭을 하면 click 이벤트가 발생하는 것처럼 $emit('event-name') 가 실행되면 event-name 이벤트가 발생
- Emit Event 흐름
  - 자식 컴포넌트에 있는 버튼 클릭 이벤트를 청취하여 연결된 핸들러 함수(childToParent) 호출
  - 호출된 함수에서 $emit을 통해 상위 컴포넌트에 이벤트(child-to-parent)를 발생
  - 상위 컴포넌트는 이벤트 (child-to-parent)를 청취하여 연결된 핸들러 함수(parentGetEvent) 호출
  - 호출된 함수에서 console.log(~) 실행
  - 한 단계만 올라갈 수 있음
- emit with data 흐름
  - 자식 컴포넌트에 있는 버튼 클릭 이벤트를 청취하여 연결된 핸들러 함수 (childToParent) 호출
  - 호출된 함수에서 $emit을 통해 상위 컴포넌트에 이벤트(child-to-parent)를 발생
    - 이벤트에 데이터(child data)를 전달
  - 상위 컴포넌트는 이벤트 (child-to-parent)를 청취하여 연결된 핸들러 함수 (parentGetEvent) 호출, 함수의 인자로 전달된 데이터(child data)가 포함
  - 호출된 함수에서 console.log('~child data~') 실행

#### pass props / emit event 컨벤션

- 아니 그래서 언제는 kebab-case고 언제는 camelCase야?
  -  ⇒ html 요소에서 사용할 때는 kebab, javascript에서 사용할 때는 camel으로 생각!
- props
  - 상위 ⇒ 하위 흐름에서 html 요소로 내려줌 : kebab 
  - 하위에서 받을 때 javascript에서받음 : camel
- emit
  - emit 이벤트를 발생시키면 html 요소가 이벤트를 청취함 : kebab 
  - 메서드, 변수명 등은 javascript에서 사용함 : camel