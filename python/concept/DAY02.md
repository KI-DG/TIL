# DAY02


### 제어문

- 조건문 
  
  - 조건문은 참/거짓을 판단하는 조건식과 함께사용
  
  - 조건이 잠인 경우이후 들여쓰기 되어잇는 코드 블록을 실행
  - 특정상황에서 사용하고 싶을 때 사용
    
    ```
    if 조건 == True:
      
    else:

    *실습*
    num = int(input()) #input()은 문자열이기 떄문에 int()로 정수로 변


    ```
    

- 복수 조건문

```
dust = int(input('입력해주세요')
if dust > 150 :
    pirnt('매우나쁨')
elif dust > 80:
    print('나쁨')
elif dust > 30:
    print('보통')
else:
    print('좋음')

```

- 중첩 조건문
  - 조건문은 다른 조건문에 중첩되어 사용 될 수 있음
  - **들여쓰기**에 유의하여 작성
  - 
```
  dust = int(input('입력해주세요')
  if dust > 150:
    pirnt('매우나쁨')
      if dust > 300:
        print('실외활동을 자제하세요')
  elif dust > 80:
    print('나쁨')
  elif dust > 30:
    print('보통')
  elif dust >= 0:
    print('좋음')
  else:
    print('다시 입력하세요')

```
- 조건 표현식
    - 삼항 연산자라고 부리기도 함
    - if 를 한줄로 - 가독성이 좋아짐 코드가 간단해짐
    - 절대값을 나타내는 코드 p25
    - *실습*
```
if num >=0:
  value = num
else:
  value = 0
  
print(value) #0
```



- 반복문
  - 특정조건을 만족할 떄까지 같은 동작을 계속 반복하고 싶을떄 사용
  - 문제를 해결할 떄까지 사용

while 문
  - 종료 조건에 해당하는 코드를 통해 반복문을 종료시켜야 함 (배가 부를때까지) - 쿠키런
  - 조건이 충족될때까지 사용
  - 참인 동안에 반복사용 == 조건식이 참인 경우 반복적으로 실행
     1. while 조건인동안 
     2. 코드 실행
     3. 조건이 맞는지 다시 확인
     4. 코드 반복
  - 무한루프를 하지 않도록 종료 조건(잘설정)이 반드시 필요
  - a += 1 == a = a +1
  
for 문
  - 반복가능한 객체를 모두 순회하면 종료(별도의 종료 조건이 필요없음) (횟수) - 점찍기
  - 선언을한 뒤 - 하나씩 꺼내서 쓴다.
  - items(): 두개 뽑아쓰는거, (key,value)의 튜플로 구성된 결과
  - enumnerate() : (index,value) 형태의 튜플로 구성된 열거 객체 순서랑 이름을 가져옴
   카운트할때 용이하다.
   print(list(enumerate(members,start=1))) index가 1부터 시작
  - list comprehension : 표현식과 저어문을 통해 특정한 값을 가진 리스트를 간결하게 생성하는 방법
  - code for 변수 in iterable
  - code for 변수 in iterable if 조건식

반복제어
- break, continue, for-else
쿠키런에서 item
- break(특정상황에서 멈추고 싶을때) 반복문종료
  - 브레이크 만나면 루프 끝
- continue 코드 블록은 수행하지 않고 다음 반복을 수행 
  - 해야하는 코드를 skip
- for -else 온전히 끝나고 실행
- pass 아무것도 하지 않음



# 함수
- Decomposition(분해) 
  - 기능을 분해하고 재사용 가능하게 만들고
  - EX) len([1,2,3]) -코드를 간편화 시켜준다.
- Abstraction(추상화)
  - 변수 

내장함수 - 파이썬 개발자가 만듬(자동설치)
외장함수 - 다른 개발자 파이썬 말고 import문을 통해 사용
사용자 정의 (내가 만든)

함수 
선언- 생성(어디다가 만들어보관한다.) 호출 - 사용(필요할 때마다 쓴다.)
입력 - 레시피 결과 - 요리
문서화 - 설명
범위 - 나중에 다시

함수의 결과값
vlid function
return 값이 없는 경우 None 을 반환하고 종료
ex) print

결과가 있는 함수
value returning function
return을 하게 되면, 값 반환 후 함수가 바로 종료
결과가 나오면 끝이남

print 와 return의 차이점
print를 사용하면 호출될때마다 값이 출력됨(주로 테스트를 위해 사용)

데이터 처리를 위해서는 return 사용
return 앞에 print를 사용 그래야 눈에도 보이고 데이터에도 적용된다.
하나의 값만 반환한다. 
두개를 사용하려면 - 반환값으로 튜플을 사용

::-1 뒤집는것

*rest  
*args (가변인자)
  * 중요 짱박는거 변경가능 지정한거 빼고 나머지는 묶어서 사용

가변 키워드인자(**kwargs) 키보드 인자가 여러개일떄
키워드인자는 딕셔너리로 묶여 처리됨 parameter에 **를 붙여 표현
문자열로 쓰면 안됨 변수처럼 써야됨

LEGB 
ex) 가족 
아버지> 어머니 > 나 > 동생 
에어컨4 리모콘1
리모콘 찾을 때 내방을 먼저 찾음
탐색하는데 내방O 그럼 끝 그러나 없으면 바로 위에 방을 탐색 거기서 찾으면 끝 그러나 없으면 바로 위에 방 가서 탐색 거기서 찾으먼 끝 그러나 없으면 마지막 거실(모두가 쓰는데)에 가서 찾음
리모콘 == 함수,변수
에어컨 == 문제
집 == 프로그램
밖 == 파이썬

map(함수이름, 데이터구조의 모든 요소) - 상자로 됨 list로 변형해야됨
filter(함수이름, 데이터구조의 모든 요소)
결과가 True인것만 넣음
zip 복수의 요소들을 모아 튜플을 원소로하는 zip object 세로로 묶는다.
lambda함수 익명함수라고 불림
return문을 가질수 없음
간편 조건문 외 조건문이나 반복문을 가질 수 없음
장점 
함수를 정의해서 사용하는 것보다 간결하게 사용 가능
def를 사용할 수 없는 곳에서도 사용가능
재귀 함수
자기 자신을 호출하는 함수 
ex) 팩토리얼 4! == 4*3*2*1
주의사항 base case에 도달할 때까지 함수를 호출함
최대 재귀 깊이가 1000번임 넘어가면 에러 발생

알고리즘 자체가 재귀적인 표현이 자연스러운 경우 재귀함수를 사용함 
변수 사용을 줄여줄 수 있음
재귀 호출은 입력값이 커질 수록 연산속도가 오래걸림

모듈
from module impor* 전부다

제어문 함수 
반복문 스코프 모듈

월요일 
저장
프로그램밍



----
프로그래밍 
저장 처리
변수 - 연산자

input 파라미터 함수 안에서 입력으로 받는것 x

함수

out put return 


