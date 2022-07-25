#  DAY06



###  이차원 리스트

이차원 리스트는 리스트를 원소로 가지는 리스트일뿐이다.



```
          0,1,2   0,1,2    0,1,2

matrix = [[1,2,3],[4,5,6],[7,8,9]]

             0      1       2
```

 이차원 리스트는 행렬이다. 



이차원 리스트의 순회

인덱스를 통해 각각 출력하면 가능하다!

```
matrix[0][0] materix[0][1]  이런식으로 가능

for i in range(3) #행 세로
	for j in range(4) #열 가로
		print(matrix[i][j], end= "")
	print()
행부터 하고 열을 함 #행 우선순회

for i in range(4) #열
	for j in range(3) # 행
		print(matrix[j][i], end = "")
	print()
#열 우선순회

알고리즘에서 더 공부해야된다.

최대값, 최소값


max_vlaue = 0

for i in range(3)
	for j in range(4)
		if matrix[i][j] > max_value:
		 	max_value = matrix[i][j]
		 	
print(max_value) 최대값

min_vlaue = 99999999
	
max_value = max(map(max,matrix))
min_value + min(map(min,matrix))
```

변수를 잘 생각해야 된다. 남들이 알아보게끔 해야되는 게 중요 **가독성**이 중요



### 아스키(ASCII) 코드

컴퓨터는 숫자만 이해할 수 있다.

| 비트(bit)           | 바이트(byte)                                  |
| ------------------- | --------------------------------------------- |
| 0,1만 읽을 수 있다. | 데이터를 저장하는 기본 단위<br />1byte = 8bit |

문자는 어떻게 읽지?

파이썬 내장함수 아스키코드를 활용하는 함수

chr(아스키코드) - 문자로변경

ord(문자) - 숫자로 변경





###  함수 

```
dictionary에서 get 활용법
a={'key':'value'}
a['key'] == value
a.get('key') == value  #결과가 같음


a.get('key', ???) = 키에 value 없을때 기본값을 보여준다 
a.get('name'), a.get('price') none이 나옴
a.get('name'), a.get('price', '비상장 주식입니다.') 비상장 주식입니다가 나옴


data.get('release_date')  [:4] #연도에 앞에 4글자만 자른다.


open 파일을 읽어올 때 사용 하는 함수 (파일 입출력)
open(파일(문자열로 받는다), 키워드 인자 = r읽는거 w 쓰는거,encoding(인코딩))
./ 내가 있는 파일(현재파일은 지워도 가능) (상대경로 - 똑같은 파일이 있을 때 사용)

json - dict랑 비슷하다. key와 value가 있는 것이다. 

json.load는 json은 dict를 변환시킨다. 

pprint() 이쁘게 출력해줄게
		 딕셔너리를 가독성 있게 출력해줄게
		 이차원리스트도 가능
		 
__name__ == __main__
현재 파일에서만 쓸수 있게 만드는 기능
```



반복문을 만든다. 

반복문에 새로운 데이터에 있는 값중에 genre_ids의 값을 각각 뽑아오고 싶다.

만일 genre_ids가 == genres(id)랑갔다면 

 genres(id) 중 각각의 genre을 뽑아 그게 


