import sys

sys.stdin = open('input')

dx = [-1, 1, 0, 0]  # 델타탐색 상, 하, 좌, 우
dy = [0, 0, -1, 1]


def bfs(x, y):
    queue = [(x, y)]
    while queue:
        x, y = queue.pop(0)     # 시작지점
        visited[x][y] = True

        for k in range(4):  # 델타탐색
            nx = x + dx[k]
            ny = y + dy[k]

            # 범위가 맞는지, 방문안했는지 확인, 통로인지 확인
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and arr[nx][ny] == 0:
                visited[nx][ny] = True      # 방문하면 True로 바꿔줌
                queue.append((nx, ny))      # 다음껄로 이동
                distance[nx][ny] = distance[x][y] + 1

            elif 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and arr[nx][ny] == 3:
                distance[nx][ny] = distance[x][y]

                return distance[nx][ny]

    return 0


t = int(input())
for tc in range(1, t + 1):

    n = int(input())  # 미로의 크기
    arr = [list(map(int, input())) for _ in range(n)]
    visited = [[False] * n for _ in range(n)]
    distance = [[0] * n for _ in range(n)]
    result = 0
    for i in range(n):
        for j in range(n):
            if arr[i][j] == 2:
                result = bfs(i, j)

    print(f"#{tc}", result)


