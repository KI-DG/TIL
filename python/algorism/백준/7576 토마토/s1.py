from _collections import deque
import sys

sys.stdin = open("input.txt")

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]


def bfs():
    while queue:
        x, y = queue.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]

            if 0 <= nx < n and 0 <= ny < m and arr[nx][ny] == 0:
                queue.append([nx, ny])
                arr[nx][ny] = arr[x][y] + 1


t = int(input())

for tc in range(1, t + 1):
    m, n = map(int, input().split())
    # 가로의 길이, 세로의 길이
    arr = [list(map(int, input().split())) for _ in range(n)]
    # 토마토 상자
    queue = deque([])

    for j in range(n):
        for i in range(m):
            if arr[j][i] == 1:
                queue.append([j, i])

    bfs()
    answer = 0
    zero = False
    for j in range(n):
        for i in range(m):
            if arr[j][i] == 0:
                zero = True
            answer = max(answer, arr[j][i])
            
    if zero:
        answer = -1
        print(f'#{tc} {answer}')
    else:
        print(f'#{tc} {answer - 1}')