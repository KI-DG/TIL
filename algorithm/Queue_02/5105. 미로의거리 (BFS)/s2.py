import sys

sys.stdin = open('input')

dx = [-1, 1, 0, 0]  # 델타탐색 상, 하, 좌, 우
dy = [0, 0, -1, 1]


def bfs(x, y):
    queue = [(x, y)]
    while queue:
        x, y = queue.pop(0)     # 시작지점
        visited[x][y] = True    # 방문했으면 True 변환

        for k in range(4):  # 델타탐색
            nx = x + dx[k]
            ny = y + dy[k]

            # 범위가 맞는지, 방문안했는지 확인, 통로인지 확인
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and arr[nx][ny] == 0:
                visited[nx][ny] = True      # 방문하면 True로 바꿔줌
                queue.append((nx, ny))      # 다음껄로 이동
                distance[nx][ny] = distance[x][y] + 1  # 다음껄로 이동하면 +1을 해준다.

            # 범위가 맞는지, 방문안했는지 확인, 도착점인지 확인
            elif 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and arr[nx][ny] == 3:
                distance[nx][ny] = distance[x][y]  # 통로의 개수만 세야 됨으로 도착지점 바로 전껄로 함
                return distance[nx][ny]

    return 0    # 도착점에 도달하지 못하면 0으로 출력


t = int(input())
for tc in range(1, t + 1):

    n = int(input())  # 미로의 크기
    arr = [list(map(int, input())) for _ in range(n)]  # 행렬을 생성
    visited = [[False] * n for _ in range(n)]   # 방문자 리스트 생성
    distance = [[0] * n for _ in range(n)]  # 크기가 n이고 숫자를 더할 리스트 생성
    result = 0   # 결과값 저장
    for i in range(n):      # 시작점을 찾을 탐색 시작
        for j in range(n):
            if arr[i][j] == 2:
                result = bfs(i, j)

	    print(f"#{tc}", result)