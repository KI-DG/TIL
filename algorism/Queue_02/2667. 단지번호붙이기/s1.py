dx = [-1, 1, 0, 0]  # 델타 검색 상, 하, 좌, 우
dy = [0, 0, -1, 1]


def bfs(x, y):  # bfs 함수 생성
    visited[x][y] = True    # 방문을 한다.
    queue = [(x, y)]    # 시작 좌표를 넣고 큐를 생성
    total = 1

    while queue:
        x, y = queue.pop(0)
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            # 지도 범위와 방문을 했는지 다음에 건물이 있는 확인
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and arr[nx][ny] == 1:
                visited[nx][ny] = True  # 방문처리
                queue.append((nx, ny))  # 다음 값을 넣우준다.
                total += 1  # 집이 있을 때마다 +1

    return total


n = int(input())  # 지도의 크기

arr = [list(map(int, input())) for _ in range(n)]  # 지도를 받아와준다.
visited = [[False] * n for _ in range(n)]  # 지도와 똑같은 사이즈의 방문 리스트
result = []  # 단지의 수를 담을 빈 리스트 생성

for i in range(n):
    for j in range(n):
        if not visited[i][j] and arr[i][j] == 1:
            result.append(bfs(i, j))

print(len(result), *sorted(result), sep="\n")
