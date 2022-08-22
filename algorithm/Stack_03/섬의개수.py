import sys

sys.setrecursionlimit(1000000)


def dfs(x, y):
    global total
    visited[x][y] = True
    total += 1

    for k in range(8):
        nx = x + dx[k]
        ny = y + dy[k]

        if 0 <= nx < height and 0 <= ny < weight and not visited[nx][ny] and borad[nx][ny] == 1:
            dfs(nx, ny)


while True:
    weight, height = map(int, input().split())

    if weight == 0 and height == 0:
        break

    borad = [list(map(int, input().split())) for _ in range(height)]
    visited = [[False] * weight for _ in range(height)]

    dx = [0, 0, 1, -1, 1, -1, -1, 1]
    dy = [-1, 1, 0, 0, -1, -1, 1, 1]
    result = []


    for i in range(height):
        for j in range(weight):
            if not visited[i][j] and borad[i][j] == 1:
                total = 0
                dfs(i, j)
                result.append(total)

    print(len(result))

