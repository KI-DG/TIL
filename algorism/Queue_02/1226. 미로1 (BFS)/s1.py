import sys

sys.stdin = open('input')

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(x, y):
    queue = [(x, y)]
    visited[x][y] = True

    while queue:
        x, y = queue.pop(0)

        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]

            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and maze[nx][ny] != 1:
                if maze[nx][ny] == 3:
                    return 1
                else:
                    queue.append((nx, ny))
                    visited[nx][ny] = True
    return 0


for tc in range(1, 11):
    n = 16
    t = int(input())
    maze = [list(map(int, input())) for _ in range(n)]
    visited = [[False] * n for _ in range(n)]
    result = 0
    for i in range(n):
        for j in range(n):
            if maze[i][j] == 2:
                result = bfs(i, j)

    print(f'#{tc} {result}')