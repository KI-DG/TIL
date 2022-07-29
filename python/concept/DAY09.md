# DAY09

API  vs  JSON

Application programming Interface (서로 다른 두개의 접점)

(client)

브라우저             요청 ->                서버

브라우저             <- 응답                서버

agify.io = API 를 보여주는 사이트



Json 데이터 하나의 형식(타입)

.json 하면 json 파일을 딕셔러니 형태로 오는거다



requests의 모듈의 메서드

.get 서버의 데이터를 조회할때(가져온다)

.post 데이터를 수정할때(만능)

.put  데이터를 변경할때

.delete 데이터를 삭제할때



http:// 프로토콜

Base Url 기본 유알엘 www. // 메뉴 제외한 공통사항 (tmdb에 보낼거다)

path 경로 어떤 메뉴 쓸거야? 

파라미터(params) ' ?' 기준으로 시작하면서 key value로 나눈다. 





**주의사항**

1. 변수, 함수명은 의미있게 짓자. (스타일 가이드를 지키자!)
2. 변수, 함수명은 스네이크 케이스 / 클래스는 캐멀 케이스
3. True/False evaluation -> 빈 컨테이너, Boolean 검사, 단 값은 무조건 그대로
4. else가 필요없는 경우 (if 문에서 else가 필요없으면 안써도 된다.)
5. 중복된 코드는 함수로 묶자.
6. 복잡한 코드는 주석을 달자. (이상적인 코드는 주석이 없이 해도 되지만 힘들다. 그러니 주석을 달아줘야 됩니다.)
