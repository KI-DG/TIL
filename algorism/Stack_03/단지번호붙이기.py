def dfs(x, y):
    global total
    visited[x][y] = True
    total += 1

    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]
        # 델타 이동
        if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and board[nx][ny] == 1:
            # 범위와 조건 숫자가 1이고 not visited
            dfs(nx, ny)


n = int(input())

board = [list(map(int, input())) for _ in range(n)]
visited = [[False]*n for _ in range(n)]
result = []     # 단지내 집에 수 모임

dx = [-1, 1, 0, 0]   # 상 하 좌 우
dy = [0, 0, -1, 1]


# 1. 이차원 리스트를 행 순회
for i in range(n):
    for j in range(n):
        if not visited[i][j] and board[i][j] == 1:  # 2. 1이면(집이면) DFS 시작
            total = 0
            dfs(i, j)    # 여기서 시작할게
            result.append(total)

print(len(result))
for i in sorted(result):
    print(i)

print(len(result), *sorted(result), sep='\n')