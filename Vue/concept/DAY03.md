# DAY03

## Vuex

### State Management

- 상태 (state) - 현재에 대한 정보(data)
- 현재 App이 가지고 있는 Data로 표현
- 여러 개의 component를 조합해서 하나의App을 만들고 있음
- 각 component는 독립적이기 때문에 각각의 상태(data)를 가짐
- 여러 개의 component가 같은 상태를 유지할 필요가 있음
  - 상태 관리 필요

#### Pass Props & Emit Event

- 각 컴포넌트는 독립적으로 데이터를 관리 
- 같은 데이터를 공유하고 있으므로, 각 컴포넌트가 동일한 상태를 유지하고 있음
- 데이터의 흐름을 직관적으로 파악가능
- component의 중첩이 깊어지면 데이터 전달이 쉽지 않음
- 공통의 상태를 유지해야 하는 component가 많아지면 데이터 전달 구조가 복잡해짐

#### Centralized Store

- 중앙 저장소에 데이터를 모아서 상태 관리
- 각 component는 중앙 저장소의 데이터를 사용
- component의 **계층에 상관없이** 중앙 저장소에 접근해서 데이터를 얻거나 변경할 수 있음
- 중앙 저장소의 데이터가 변경되면 각각의 component는 해당 데이터의 변화에 반응하여 새로 변경된 데이터를 반영함
- 규모가 크거나 컴포넌트 중첩이 깊은 프로젝트의 관리가 매우 편리

### Vuex

- state management pattern + Library (상태 관리 패턴 + 라이브러리)
- 중앙 저장소를 통해 상태 관리를 할 수 있도록 하는 라이브러리
- 데이터가 예측 가능한 방식으로만 변경 될 수 있도록 하는 ***규칙을 설정하며***, Vue의 반응성을 효율적으로 사용하는 상태 관리 기능을 제공
- Vue의 공식 도구로써 다양한 기능을 제공

```vue
vue create vuex-app
// 프로젝트 생성
cd vuex-app  
// 디렉토리 이동
vue add vuex 
// Vue CLI를 통해 vuex plugin 적용
```

- 핵심 컨셉 4가지
  1. state
  2. getters
  3. mutations
  4. actions

#### State

- 중앙에서 관리하는 모든 상태 정보
- 개별 component는 state에서 데이터를 가져와서 사용
  - 개별 component 가 관리하던 data를 중앙 저장소에서 관리하게 됨
- state의 데이터가 변화하면 해당 데이터를 사용하는 component도 자동으로 다시 렌더링
- store.state로 state 데이터에 접근

#### Mutations

- state를 변경하기 위한 methods
- 실제로 state를 변경하는 유일한 방법
- vue 인스턴스의 methods에 해당하지만 Mutaitons에서 호출되는 핸들러 함수는 반드시 동기적이어야 함
  - 비동기 로직으로 mutations를 사용해서 state를 변경하는 경우, state의 변화의 시기를 특정할 수 없기 때문
- 첫 번째 인자로 state를 받으며, component 혹은 Actions에서 commit() 메서드로 호출됨
- actions 에서 commit()을 통해 mutations 호출한다.
  - mutations는 state를 변경하는 유일한 방법
  - component 또는 actions에서 commit()에 의해 호출됨
- commit(A, B)
  - A: 호출하고자 하는 mutaitions 함수
  - B: payload

#### Actions

- 비동기 작업이 포함 될 수 있는 (외부 API 와의 소통) methods
- state를 변경하는 것 외의 모든 로직 진행
- mutations와 비슷하지만 비동기 작업을 포함할 수 있다는 차이가 있음
- state를 직접 변경하지 않고 commit() 메서드로 mutaitons를 호출해서 state를 변경함
- context 객체를 인자로 받으며, 이 객체를 통해 stre.js의 모든 요소와 메서드에 접근할 수 있음
- component에서 dispatch() 메서드에 의해 호출됨
- context (첫 번째 인자)
  - context는 store의 전반적인 속성을 모두 가지고 있으므로 context.state와 context.getters를 통해 mutations를 호출하는 것이 모두 가능
  - dispatch()를 사용해 다른 actions도 호출할 수 있음
  - 단 actions에서 state를 직접 조작하는 것은 삼가해야 함
- payload (두번째 인자)
  - 넘겨준 데이터를 받아서 사용

#### Getters

- state를 활용해 계산한 새로운 변수 값
- vue 인스턴스의 computhed에 해당
- state를 활용하여 계산된 값을 얻고자 할 때 사용 state의 원본 데이터를 건들지 않고 계산된 값을 얻을 수 있음
- computed와 마찬가지로 getters의 결과는 캐시 되며, 종속된 값이 변경된 경우에만 **재계산됨**
- getters에서 계산된 값은 state에 영향을 미치지 않음 
- 첫번째 인자로 state, 두번째 인자로 getter를 받음



- component에서 데이터를 조작하기 위한 데이터의 흐름
  - component  => (actions) => mutations => state
- component에서 데이터를 사용하기 위한 데이터의 흐름
  - state => (getters) => component



- html에서 호출하는 코드는 좋은 코드가 아니다

### Lifecycle Hooks

- 각 Vue 인스턴스는 생성과 소멸의 과정 중 단계별 초기화 과정을 거침
  - Vue 인스턴스가 생성된 경우, 인스턴스를 DOM에 마운트하는 경우, 데이터가 변경되어 DOM를 업데이트 하는 경우
- 각 단계가 트리거가 되어 특정 로직을 실행할 수 있음

#### created

- Vue instance가 생성된 후 호출됨
- data, computed 등의 설정이 완료된 상태
- 서버에서 받은 데이터를 vu instance의 data에 할당하는 로직을 구현하기 적합
- mount되지 않아 요소에 접근할 수 없음

#### mounted

- Vue instance가 요소에 mount된 후 호출됨
- mount된 요소를 조작할 수 있음

#### updated

- 데이터가 변경되어 DOM에 변화를 줄 때 호출됨

#### 특징

- instance마다 각각의 Lifecycle을 가지고 있음

- Lifecycle Hooks는 컴포넌트별로 정의할 수 있음
- 부모 컴포넌트의 mounted hook이 실행 되었다고 해서 자식이 mount 된 것이 아니고, 부모 컴포넌트가 updated hook이 실행 되었다고 해서 자식이 updated 된 것이 아님
  - 부착 여부가 부모- 자식 관계에 따라 순서를 가지고 있지 않은 것
- instance마다 각각의 Lifecycle을 가지고 있기 때문

### Local Storage

#### window.localStorage

- 브라우저에서 제공하는 저장공간 중 하나인 Local Storage에 관련된 속성
- 만료되지 않고 브라우저를 종료하고 다시 실행해도 데이터가 보존됨
- 데이터가 문자열 형태로 저장
- 관련 메서드 
  - setItem(key, value) - key, value 형태로 데이터 저장
  - getItem(key) - key에 해당하는 데이터 조회