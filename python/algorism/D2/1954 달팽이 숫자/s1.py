import sys

sys.stdin = open("input.txt")

dx = [0, 1, 0, -1]    # 우 하 좌 상
dy = [1, 0, -1, 0]

t = int(input())

for tc in range(1, t + 1):
    n = int(input())

    arr = [[0] * n for _ in range(n)]

    x, y = 0, 0    # 출발위치
    direction = 0  # 처음 출발방향

    for i in range(1, n * n + 1):
        arr[x][y] = i

        nx = x + dx[direction]   # x의 다음 값 지정
        ny = y + dy[direction]   # y의 다음 값 지정

        if 0 <= nx < n and 0 <= ny < n and arr[nx][ny] == 0:      # 범위를 벗어나지 않고 0이 면
            x = nx                                                # x, y 값을 바꿔주고
            y = ny
        else:
            direction = (direction + 1) % 4                      # 범위를 벗어나거나 이미 숫자가 있으면 방향을 바꿔준다
            x += dx[direction]
            y += dy[direction]

    print(f'#{tc}')
    for line in arr:
        print(*line)
