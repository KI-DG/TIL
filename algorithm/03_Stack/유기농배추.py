import sys

sys.setrecursionlimit(1000000)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def dfs(x, y):
    visited[x][y] = True

    for z in range(4):
        nx = x + dx[z]
        ny = y + dy[z]

        if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and borad[nx][ny] == 1:
            dfs(nx, ny)


t = int(input())

for tc in range(1, t + 1):
    m, n, k = map(int, input().split())
    # m == 가로길이 n == 세로길이 k == 배추숫자
    borad = [[0] * m for _ in range(n)]
    visited = [[False] * m for _ in range(n)]

    for _ in range(k):
        a, b = map(int, input().split())
        borad[b][a] = 1

    total = 0
    for i in range(n):
        for j in range(m):
            if not visited[i][j] and borad[i][j] == 1:
                dfs(i, j)
                total += 1

    print(total)
