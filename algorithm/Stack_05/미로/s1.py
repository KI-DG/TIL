import sys

sys.stdin = open('input')

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def maze(x, y):
    global result
    vistied[x][y] = True

    for z in range(4):
        nx = x + dx[z]
        ny = y + dy[z]
        if 0 <= nx < n and 0 <= ny < n and arr[nx][ny] == 3:
            result = 1
            return
        if 0 <= nx < n and 0 <= ny < n and not vistied[nx][ny] and arr[nx][ny] == 0:
            maze(nx, ny)


t = int(input())

for tc in range(1, t + 1):
    n = int(input())    # 미로의 크기
    arr = [list(map(int, input())) for _ in range(n)]   # 주어진 미로를 만들어준다.
    vistied = [[False] * n for _ in range(n)]   # 방문했는지 안했는지 확인해준다.
    result = 0

    for i in range(n):
        for j in range(n):
            if arr[i][j] == 2:
                maze(i, j)   # 시작점

    print(f"#{tc} {result}")