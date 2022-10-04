# DAY03

1. venv의 환경을 만들어 준다 - venv (가상 환경)
2. venv를 활성화 시켜 준다.
3. 가상 환경 비활성화 하는 법
4. django 설치
5. 가상 환경 패키지 목록 조회
6. requirements.txt 생성
7. django 프로젝트 생성
8. django 서버 실행
9. django 애플리케이션 생성 - settings.py
10. URL 생성 (상속)
11. Views 생성
12. Templates 생성(상속) - settings.py
13. model 작성
14. makemigrateions
15. migrate - ipython, django_extensions
16. 함수에 값을 가지고 오는 함수 만들기
17. 제일 처음화면에 다 나오게 하기 
18. python manage.py shell_plus
19. create.html을 삭제
20. post로 바꿔준다 {% csrf_token %}
21. detail만들기
22. delete만들기
23. 수정만들기

### CREATE

- redirect

  - index 페이지로 돌아가도록 하는데 render를 이용하면 index페이지만 보여주고, 주소도 바뀌지가 않는다
  - 이 두가지의 문제를 해결하기 위해서는 redirect를 이용하면 된다

- GET

  - 조회

- POST

  - 생성
  - 수정
  - 삭제
  - 데이터베이스 변화
  - 주소에 값을 감추고 HTTP body에 저장한다. (http://127.0.0.1:8000/articles/create/) 이렇게만 나온다 정보를 들어나지 않게 해킹의 위험에서 벗어나기 위해서 필요하다

  - CSRF 공격 방어 
  - {% csrf_token %} - POST에서 무조건 써야된다
    - 너가 진짜 요청보낸거 맞는지 확인하기 위해서 사용
    - 토큰이 같이 보내진다
  - form으로만 가능 method=post를 사용하기위해 이것만 가능 

### Admin site

- 관리자 페이지가 이미 있다.
- 서버의 관리자가 활용하기 위한 페이지 

```python 
python manage.py createsuperuser
```

-------

