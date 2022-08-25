import sys

sys.stdin = open('input')

dx = [-1, 1, 0, 0]  # 델타탐색 상, 하, 좌, 우
dy = [0, 0, -1, 1]


def bfs(x, y):
    queue = [(x, y)]
    while queue:
        x, y = queue.pop(0)     # 시작지점

        for k in range(4):  # 델타탐색
            nx = x + dx[k]
            ny = y + dy[k]

            # 범위가 맞는지, 방문안했는지 확인, 벽이 아닌지 확인
            if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == 0 and arr[nx][ny] != 1:
                if arr[nx][ny] == 3:  # 도착점인지 확인
                    visited[nx][ny] = visited[x][y]
                    return visited[nx][ny]
                queue.append((nx, ny))     # 다음껄로 이동
                visited[nx][ny] = visited[x][y] + 1  # 다음껄로 이동하면 +1을 해준다.

    return 0    # 도착점에 도달하지 못하면 0으로 출력


t = int(input())
for tc in range(1, t + 1):

    n = int(input())  # 미로의 크기
    arr = [list(map(int, input())) for _ in range(n)]
    visited = [[0] * n for _ in range(n)]
    result = 0
    for i in range(n):
        for j in range(n):
            if arr[i][j] == 2:
                result = bfs(i, j)

    print(f"#{tc}", result)


