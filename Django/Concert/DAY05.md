# DAY05

### Authentication system

- Authentication (인증)
  - 신원확인
  - 사용자가 자신이 누구인지 확인하는 것
- Authorization ( 권한, 허가)
  - 권한 부여
  - 인증된 사용자가 수행할 수 있는 작업을 결정

#### AUTH_USER_MODEL 

- 프로젝트에서 User를 나타낼 때 사용하는 모델
- 프로젝트가 진행되는 동안 (모델을 만들고 마이그레이션 한 후) 변경할 수 없음

#### custom User model 대체

````python
accounts/models.py
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
	pass

crud/settings.py
AUTH_USER_MODEL = 'accounts.User'

accounts/admin.py
from django.contrib.auth.admin import UserAdmin
from .models import User

admin.site.register(User, UserAdmin)
````

1. 대체할 유저 클래스를 만든다
2. 프로젝트에게 대체할 유저가 이거다라고 알려주기
3. UserAdmin을 등록

[참고]

- AbstractUser
  - 관리자 권한과 함께 완전한 기능을 가지고 있는 User model을 구현하는 추상 기본 클래스
  - 몇 가지 공통 정보를 여러 다른 모델에 넣을 때 사용하는 클래스
  - 데이터베이스 테이블을 만드는 데 사용되지 않으며, 대신 다른 모델의 기본 클래스로 사용되는 경우 해당 필드가 하위 클래스의 필드에 추가 됨

[주의]

- 모델 관계에 영향을 미치기 때문에 훨씬 더 어려운 작업이 필요 
  - 변경사항이 자동으로 수행될 수 없기 때문에 DB 스키마를 직접 수정하고, 이전 사용자 테이블에서 데이터를 이동하고, 일부 마이그레이션을 수동으로 다시 적용해야 함
- 중간 변경은 권장하지 않음 

#### 데이터 베이스 초기화

1. migrations 파일 삭제 
   - 폴더 및 init.py 삭제 금지 
2. db.sqlite3 삭제
3. 다시 migtrations 진행