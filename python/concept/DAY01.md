# DAY01
## 파이썬
- 사람이 이해할 수 있는 문자로 구분
- 기본적인 규칙과 문법이 존재
  소스코드 
  프로그래밍 언어로 작성된 프로그램
  번역기(interpreter or comliler)
  소스코드를 컴퓨터가 이해할 수 있는 기계어로 번역
  파이썬의 경우 인터프리터를 사용
  배워야 하는 이유 

1. 알고리즘 코딩 테스트에 유리
   알고리즘 코딩 테스트에서는 파이썬이 2위 기록
   코딩 테스트의 유형이 다양해지면서, 변칙적인 유형에 대응하기 쉬운 파이썬이 유리
   대회 준비를 위한다면 C를 추천 입사를 위한 코딩테스트는 파이썬 - 사람과 친화 
2. 구현 코딩테스트에 유리
   유용한 라이브러리 중 최소한만 사용해 프로그램을 개발할 수 있어 가장 유리한 언어
   실행 시간이 매우 중요한 문제 유형이 아닌 이상 파이썬으로 코딩테스트를 준비하는 것이 최선의 선택
   현업 - 서비스,프로그램
3. 가장 인기 많은 언어
   AI 개발, 테이터 분석, 웹 프로그래밍, 업무 자동화, 등 파이썬 활용 분야가 늘어남
   Easy to learn 그나마 
   파이썬은 다른 프로그램밍 언어보다 문법이 간결하고, 유연함
   비교적 쉽게 마스터하고, 프로그래밍 사고에 집중할 수 있음
   인터프리터 언어 
   파이썬은 소스 코드를 기계어로 변환 할때 통역 하듯이 1줄씩 변화

객체 지향 프로그래밍
현대 프로그래밍의 기본적인 설계 방법론으로 자리잡은 객체 지향 프로그래밍
파이썬은 객체 지향 언어이며, 모든 것이 객체로 구현되어 있음
-자세한건 나중에 학습!
IDE(intergrated development environment)
통합 개발 환경의 약자로 개발에 필요한 다양하고 

alt + 클릭 = 여러줄 쓸 수 있다.
alt +ctrl+ 방향키 = 여러줄 쓸수 잇다.
alt + 화살표 = 줄 이동
alt shift 화살표 복사
빨간색 잘못된것


기초문법
코드 스타일 가이드
코드를 어떻게 작성할지에 대한 가이드 라인
파이썬에서 제안하는 스타일 가이드 
PEP8
각 회사/프로젝트마다 따로 스타일 가이드를 설정하기도 함
 Google style guide

스타일가이드를 지켜야 된다.
들여쓰기
Space senstitive
문장을 구분할때 중관호 대신 들여씨기를 사용
들여쓰기를 할 때는 4칸 혹은 1탭을 사용

주석
코드에 대한 설명
코드를 보다 이해하기 쉽게 하여 분석 및 수정 용이해짐
주석은 코드에 영향을 주지 않으며, 개발자를 위한것
초기부터 들여야 할 가장 중요한 습관
개발자에게 주석을 다는 습관은 매우 중요
잘달린 주석은 그 어떤 정보보다 유용함
주석은 실행에 영향을 안줌
한줄 주석
주석으로 처리될 내용 앞에 #을 입력
한줄을 온전히 사용 할 수 도 있고 코드 뒷부분에 작성가능

여러줄 주석 
한줄식 #사용
""" ''' 으로 묶어서 표현
주석의 장점
개발자에게 주석을 다는 습관은 중요
코드의 내용을 잘 이해할 수 있도록 작성
가독성을 저해할 정도로 무분별한 사용은 자제
코드를 쉽게 이해할 수 있어서 코드 수정 및 협업에 유리

변수 
일상생활에서 안씀
데이터(정보,값)를 담는 상자

데이터 저장 - 처리 

데이터를 저장하기 위해서 사용
변수를 사용하면 복잡한 값들을 쉽게 사용할 수 있음(추상화)
동일 변수에 다른 데이터를 언제든 할당(저장)할 수 잇기 때문에, 변수라고 불림

변수를 사용해야 하는 이유
코드의 가독성 증가 
숫자를 직접 적지 않고 의미 단위로 작성 가능
코드 수정이 용이해짐 - 아메리카노 가격이 변경되더라도 1곳만 수정하면됨

변수의 할당
변수는 할당 연산자 = 를 통해 값을 할당 = 저장의 의미 == 같다
값은 값을 동시에 할당 할 수 있음
다른값을 동시에 할당 할 수 있음 A , B = 2000, 3000

각 변수의 값을 바꿔서 저장하기 
임시 변수활용 (자바)
x=10 y =20

tmp = x
x =y
y = tmp
print(x,y) #20, 10

pythonic
x,y = 10, 20
y,x = x, y
pritn(x,y) #20, 10

식별자 
변수 이름 규칙
식별자의 이름은 영문 알파벳, 언더스코어_ 숫자로 구성
첫글자에 숫자가 올 수 없음
길이제한이 없고, 대소문자를 구별
다음의 키워드는 예약어로 사용할 수 없음

내장 함수나 모듈 등의 이름도 사용하지 않아야 함 - 다른곳에서 쓰는 이름X
동작을 예상 할 수 없게 임의로 값을 할당하게 되므로 범용적으로 사용이 어려움

산술연산자 기본적인 사칙연산 및 수식 계산
+덧셈
-뺄셈
*곱셈
/나눗셈
// 몫
**거듭제곱

연산자 우선순위
수학에서 우선순위와 같은 
괄호가 가장 먼저 계산되고 그다음에 *와 /가 +, -보다 먼저 계산됨

자료형 분류 
프로그래밍에서는 다양한 종류의 값(데이터)를 쓸 수 있음
사용할 수 있는 데이터의 종류들을 자료형이라고 함 
boolean type 참/거짓
numeric type 숫자
string type 문자열

수치형 
int (정수, interger)
float(부동소수점, 실수 ,floating point number)

정수 자료형(int)
0,100,-200 과 같은 정수를 표현한다.
진수 표현
2진수(b inary) 0b
8진수(o ctal) 0o
16진수(he x adecimal) 0x

실수 자료형 
유리수와 무리수를 포함하는 실수를 다루는 자료형
0.1
주의 할점 (부동소수점)
실수의 값을 처리할 때 의도하지 않은 값이 나올 수 있음
연산의 결과가 0.1이아니다

원인은 부동 소수점 떄문
컴퓨터는 2진수를 사용, 사람은 10진법을 사용
이떄 10진수 0.1은 2진수로 표현하면 0.00011001...무한대로 반복
무한대 숫자를 그대로 저장할 수 없어서 사람이 사용하는 10진법의 근사값만 표시
0.1의 경우 3602879701896397/2**55 이며 0.1에 가까지만 정확히 동일하지는 않다.
이런과정에서 예상치 못한 결과가 나타남(이런 증상을 Floating point rounding error 라고함 
해결책
값 비교하는 과정에서 정수가 아닌 실수면 주의할 것
매우 작은 수보다 작은지 확인하거나 math 모듈 활용

문자열 자료형의 정의
모든 문자는 str 타입
문자열은 작은 따옴표나 큰 따옴표를 활용하여 표기
문자열을 묶을 때 동일한 문장부호를 활용
pep8에서는 소스코드 내에서 하나의 문장부호를 선택하여 유지하도록 함

중첩 따옴표
작은 따옴표가 들어있는 경우는 큰 따옴표로 문자열생성
큰 따옴표가 들어있는 경우는 작은 따옴표로 문자열생성
삼중 따옴표
따옴표 안에 따옴표를 넣는다 여러줄로 사용할때 편하다

Escape sequence
역슬래시 뒤에 특정문자가 와서 특수한 기능을 하는 문자 조합 shift + \

````\n 줄바꿈
\t 탭
\r 캐리지 리턴
\o 널
\\ \  
\' 단일인용부호
\" 이중인용부호
```

문자열 연산 
숫자는 합계가 나오는 영어로는 String concatenation 이라고 함 문자열 연결함

곱셉 
문자열 python*3
pythonpythonpython 이렇게 출력

string interpolation(문자열을 변수를 활용하여 만드는 법)
옛날 버전

str.format()

import datetime 날짜 시간
today = datetime.datetime.now() 현시간
print(today)

print(f'오늘은 {today:%y}년 {today:%m}월 {today:%d}일')
````
