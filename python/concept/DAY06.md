# DAY06

#### 컨테이너 

- 시퀀스 형(순서 != 정렬) 
- 비시퀀스 형
  - for  - iterable(반복가능한)
    - mutable - list, set dictionary (수정가능한)
    - immutable - 튜플. 레인지 (수정불가능한)

#### 함수 vs 메서드 

- 함수 - 모든 자료형이 쓸수 있는것 ex)sum, len

- 메서드 - 특정 자료형에 속해 있는것 ex) 자료형.메서드()

sort 와 replace의 차이

```
a = [3,1,2]

a.sort

print(a) 

 [1,2,3,]

b = 'hello'

b.replace("h","j")

'jello'

print(b)

'hello'
```

차이는 리스트는 mutable이고 문자열은 immutable이기 때문에 

#### 얕은 복사와 깊은 복사의 차이

```
a = 'hello'

a += 'python'

print(a) = 'hello python' # a는 문자열이라 새로운 문자열을 담아지게 되는것이다.
```

**중요**

1. 할당
2. 얕은 복사 
3. 깊은 복사 

```
1. 할당
a = [1,2,3]
b = a
print(a,b)
[1,2,3],[1,2,3]
b[0] = 4
print(a,b)
[4,2,3][4,2,3] #파이썬에서는 변수가 box가 아니다.post-it이다.

a = 'hello'
b = a
a += 'python'
print(a,b)
hellopython hello # mutable과 immutable의 차이
```

```
2. 얕은복사 #리스트에서 바뀌게 하고 싶지 않을때
a = [1,2,3]
b = a[:] # == a[0:3]
b[0] = 4
print(a,b)
[1,2,3][4,2,3]
b = list(a)
#리스트안에 리스트가 있을경우 (이차원 리스트)
3. 깊은복사
a = [1,2,[5,6]]
b = a[:]
print(a,b)
[1,2,[5,6]][1,2,[5,6]]
a[2][0] = 7
print(a,b) 
[1,2,[7,6]][1,2,[7,6]] python tutor #하나의 리스트 이기 때문에 같이 변한다.

import copy
a = [1,2,[5,6]]
b = copy.deepcopy(a)
a[2][0] = 7
print(a,b)

a = [[0]*3]*3 # 하나의 리스트 이기 때문에
a =[[0]*3 for i in range(3)] #int는 immutable이기 때문에
```