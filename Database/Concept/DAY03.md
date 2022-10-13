# DAY03

## Many to many relation ship

- target model
  - 관계 필드를 가지지 않은 모델
- source model
  - 관계 필드를 가진 모델

#### intro 정리

- M:N 관계로 맺어진 두 테이블에는 변호가 없음
- Django의 ManyToManyField은 중개 테이블을 자동으로 생성함
- Django의 ManyToManyField는 M:N 관계를 맺는 두 모델 어디에 위치해도 상관없음
  - 대신 필드 작성 위치에 따라 참조와 역참조 방향을 주의할 것

#### ManyToManyField

- 다대다 관계 설정시 사용하는 모델 필드 
- 하나의 필수 위치인자가 필요
- arguments
  - related_name
    - ForeignKey의 related_name과 동일
  - through
    - 중개 테이블을 직접 작성하는 경우, through 옵션을 사용하여 중개 테이블을 나타내는 Django모델을 지정
    - 일반적으로 중개 테이블에 추가 데이터를 사용하는 다대다 관계와 연결하려는 경우 사용됨
  - symmetrical
    - 기본 값 : True(대칭관계일때)
    - ManyToManyField 가 동일한 모델을 가리키는 정의에서만 사용
    - 팔로우 - 팔로잉 관계 (대칭관계 )
    - 대칭을 원하지 않는 경우 False로 설정
- Related Manager
  - N:1 혹은 M:N 관계에서 사용가능한 문맥
  - 역참조시에 사용할 수 있는 manager를 생성
    - 이전 모델 생성 시 objects 라는 매니저를 통해 queryset api 를 사용했던 것처럼 related manager를 통해 queryset api 를 사용할 수 있게 됨
  - 같은 이름의 메서드여도 각 관계 (N:1, M:N)에 따라 다르게 사용 및 동작
    - N:1 에서는 target 모델 객체만 사용가능
    - M:N 관계에서는 관련된 두 객체에서 모두 사용 가능
  - 메서드 
    - add(), remove(), create(), clear(), set()

#### M:N(Article-User)

#### M:N(User-User)



