import sys

sys.stdin = open('input')

board = dict()
visited = [[0] * 5 for _ in range(5)]

for i in range(5):
    arr = list(map(int, input().split()))
    for j in range(5):
        board[arr[j]] = (i, j)

cnt = 0
for i in range(5):
    arr = list(map(int, input().split()))
    for j in range(5):
        cnt += 1                                        # 몇번째인지 알기 위해 숫자를 부르면 +1

        if arr[j] in board:                             # 방문 기록
            visited[board[arr[j]][0]][board[arr[j]][1]] = 1

            bingo = 0
            diamond = 0
            x_diamond = 0
            for k in range(5):
                if sum(visited[k]) == 5:                # 가로검사
                    bingo += 1
                if sum([a[k] for a in visited]) == 5:   # 세로검사
                    bingo += 1
                if visited[0 + k][4 - k]:               # 대각선
                    diamond += 1
                if visited[k][k]:                       # 역 대각선
                    x_diamond += 1
            if diamond == 5:
                bingo += 1
            if x_diamond == 5:
                bingo += 1
            if bingo >= 3:                              # 3 빙고이면 아웃
                print(cnt)
                exit(0)