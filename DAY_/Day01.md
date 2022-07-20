# DAY01
- ## **Git** 이란 무엇인가?
  
    분산 버전 관리 프로그램
    
   ### WHY? 왜 써야 될까?
 
    예시) 우리가 파일을 보관 할때 어떻게 보관하나?
 
   - 마케팅 관리 과제.pptx
   - 마케팅 관리 과제(마지막).pptx
   - 마케팅 관리 과제(진짜마지막).pptx
   - 마케팅 관리 과제(진짜진짜마지막).pptx
  
  이러면 다른 사람이 봤을 때 잘 모른다.

  버전관리 업그레이드를 해보자

  그럼 어떻게 해야 될까? - 날짜를 적어보자 

  그럼 페이지가 1000장이면 수정된게 뭔지 어찌 알지? - 수정된 파일과 수정된 부분을 따로 기입하자

  그럼 페이지가 10억장이면 용량이 너무 커지는 거 아니야? - 마지막 파일과 수정된 부분만 기입하자 
  
   1.뉘앙스 - 2.시간 - 3.변경상항 - 4.맨 마지막 파일과 변경사항만 남겨둠

  이걸 하나하나 하기에는 인간이 너무 힘들다. 소프트웨어인 Git이 이를 도와준다.

  6하원칙에 맞게 작성해준다. 하지만 이유는 인간이 써준다.

  Git을 공부해야 되는 이유 

  **복원** **백업** **협업** 을 이룰 수가 있다.

  git  ≠  github

  git  ↔  SVN (중앙집중식 버전관리 프로그램)

  SVN의 단점

  - 하나의 저장소가 망가지면 복구할 수가 없다.
- ## Command
  - git config --global user.name "github닉네임"(최초 1회- 다른사람이 쓰면 다시인증)(육하원칙 중 누가)
  - git config --global user.email "github가입이메일"(최초 1회- 다른사람이 쓰면 다시인증)
  - git config --global --list 위의 작업이 잘 되었는지 확인하는 방법
  - git config --global -1 위의 작업이 잘 되었는지 확인하는 방법
  - git init (저장소 초기화, git으로 관리한다는 뜻)
    
    1. master가 뜨는가?
    2. Initialized가 뜨는가?
  - git add "추가하려는 파일이나 폴더" (저장은 필수)
  - git add . (모든 파일 추가)
  - git status 지금의 상태를 보여줌 (자주사용하는 습관을 들여야 됨)
  - git commit -m (working directory - stagin area로 이동 시켜줌) 버전 생성 m(다음에 이유를 적어주면 됨)
  - git log 커밋 기록 표시 
     - --oneline 한줄로만 요약해서 보여줌
      - --graph : 브랜치와 머지 내역을 그래프로 보여줍니다.
      -  --all : 현재 브랜치를 포함한 모든 브랜치의 내역을 보여줍니다.
      - --reverse : 커밋 내역의 순서를 반대로 보여줍니다. (최신이 가장 아래)
      -  -p : 파일의 변경 내용도 같이 보여줍니다.
      -  -2 : 원하는 갯수 만큼의 내역을 보여줍니다. (2 말고 임의의 숫자 사용 가능)
  - git remote add origin <github http 주소>
  - git push origin master (github로 보내줌)
  - U : untracked : 추적되지 않음
  - A : index Added : Staging Area에 들어간 상태
  - Staging Area가 존재하는 이유(Git의 꽃)
    - 내가 원하는 파일만 골라서 Commits에 보낼 수 있다.
    - 충돌 해결

----
## CLI, GUI

  CLI command line interface = GUI Graphic user interface

mkdir text = 폴더 만들어

ls = 지금 리스트 뭐가 있냐 
 - -a = 숨긴파일이랑 폴더까지 다 보여줌

cd = 폴더로 옮긴다
  - cd .. = 위로가기(폴더로 가는거) 경로 - 절대경로(주소)랑 상대경로(옆에 머있다)로 나뉜다// C드라이브 - root  절대경로//.은 나 .. 분모  상대경로 //뒤로가기(방금까지 있던곳으로 가는거)

touch = 파일을 만든다

rm = 파일을 지운다 (remove약자)
 - -r (recursive) 폴더를 지울때

control + L 맨밑으로 간다.

markdown = 텍스트 기반의 경량 마크업 언어

마크업 = markup  html의 m = markup = 역할을 부여하는것 여기서

여기까지 제목이고 여기서 여기까지 본문이야  h3=제목 p=본문

markdown - markup의 일종 쉽게 도와주는 역할

