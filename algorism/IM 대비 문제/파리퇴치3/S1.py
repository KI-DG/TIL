dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

di = [-1, -1, 1, 1]
dj = [1, -1, 1, -1]

import sys

sys.stdin = open("input")

t = int(input())

for tc in range(1, t + 1):
    n, m = map(int, input().split())

    arr = [list(map(int, input().split())) for _ in range(n)]

    maxV = 0

    for i in range(n):
        for j in range(n):
            cnt1 = arr[i][j]      # i,j 를 중심으로 + 모양
            for k in range(4):
                for z in range(1, m):
                    nx = i + dx[k] * z
                    ny = j + dy[k] * z
                    if 0 <= nx < n and 0 <= ny < n:
                        cnt1 += arr[nx][ny]
            if maxV < cnt1:
                maxV = cnt1

            cnt2 = arr[i][j]
            for k in range(4):
                for z in range(1, m):
                    nx = i + di[k] * z
                    ny = j + dj[k] * z
                    if 0 <= nx < n and 0 <= ny < n:
                        cnt2 += arr[nx][ny]
            if maxV < cnt2:
                maxV = cnt2

    print(f'#{tc} {maxV}')
