# DAY03

## Flexbox

- 하나의 축을 두고 정렬을 하고 싶다.(수직 수평정렬)

- 방향이라고 생각하면 안된다.(ex)오른쪽에서 왼쪽X 왼쪽에서 오른쪽 X

- 메인 축, 교차 축 (어떻게 쌓이는 지에 따라 메인 축 교차 축이 바뀜, 아이템이 쌓이는 방향)

- 대원칙 부모에서 자식까지만 적용 가능 자손까지 상속이 안된다.

- 속성이 나뉜다.

  - 부모 컨테이너

  ```HTML
  display: flex;
  flex-direction: column;
  flex-dircetion: row-reverse;(reverse가 있는 이유 오른쪽부터 왼쪽으로 쓰는 언어가 있다.)
  flex-wrap: wrap; 아래로 내려간다.
  flex-wrap: nowrap; 크기가 줄어들지 내려가지 않는다.
  flex-flow: row wrap;(flex-direction, flex-wrap을 합친거)
  
  justify-content 메인 축    <-> align- 교차 축(메인 축에 수직인 다른 축)
   	   -flex-start
         -flex-end
         -center
         -space-between 양쪽에 붙이고 간격이 균등하다.
         -sapce-evenly 양쪽에 안붙이고 간격의 크기가 같다.
         -space-around items 양쪽 공백의 크기가 같다.
      
  align-items 교차 축을 중심으로 어디다가 둘지 정하는 것
       - flex-start
       - flex-end
       - center
       - baseline
  
  justify-content: center;
  align-items: center; 두개를 같이 쓰면 중앙 정렬
      
  content - 여러개, items - 한개
  align-content 여러줄 정렬
      
  
  ```

   

  - 자식 아이템

    ```html
    flex-grow 비율을 지정해서 여백을 채운다, 선언을 안하면 0
    
    align-self: cneter; 적용되는 하나만 이동
    
    order:1; 작은 숫자 일수록 앞으로 순서를 정해준다. 요소는 바뀌지 않는다.
    ```

  - 