import sys

sys.stdin = open("input.txt")

t = int(input())

for tc in range(1, t + 1):
    n, k = map(int, input().split())

    board = [list(map(int, input().split())) for _ in range(n)]   # 배열을 가지고 오는 변수
    answer = 0   # 결과 값을 나타나는 변수생성

    for i in range(n):                   # 이중리스트이기때문에 이중 for 문을 사용
        cnt = 0                          # 글자의 크기를 알아 보기 위해
        for j in range(n):
            if board[i][j] == 1:                 # 가로 검사
                cnt += 1
            if board[i][j] == 0 or j == n - 1:   # 벽에 막히거나 마지막에 도달하면
                if cnt == k:                     # 들어갈 단어의 길이와 같다면
                    answer += 1                  # 값에 1을 더해주고
                cnt = 0                          # 초기값을 돌려준다
        for j in range(n):
            if board[j][i] == 1:                 # 세로 검사
                cnt += 1
            if board[j][i] == 0 or j == n - 1:
                if cnt == k:
                    answer += 1
                cnt = 0

    print(f'#{tc} {answer}')