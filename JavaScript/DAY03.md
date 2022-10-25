# DAY03

### this

- window 
  - 객체 (key : value)형태로 이루워짐
  - 전역객체 (global)

- this는 전역에서는 window
- 함수 - 함수 로서는 window
- 함수 - 메서드 로서는 앞 객체 (`.` 앞에 객체를 나타냄)
- 다시 한번 변수를 만들어서 호출해줬다
- bind를 통한 명시 
- 화살표 함수는 상위의 this (호출 기준이 아니라 선언 기준이다)
- 화살표 함수는 상위 this를 가르킨다 (위에서 가르키는 것을 똑같이 가르킨다)
- 콜백함수에서의  this는 각각 다름
  - 일반적으로 콜백 함수도 함수 호출이므로 this는 전역 객체
  - addEventListener 에서 콜백 함수 안의 this는 이벤트가 발생하는 html 요소
  - 콜백 함수를 제어하는 함수에서 this를 명시적으로 지정 가능한 것도 있음(ex. Array Helper Method)