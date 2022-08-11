import sys

sys.stdin = open("input.txt")

t = int(input())
for tc in range(1, t+1):
    n = int(input())

    arr = [[0] * n for _ in range(n)]
    x, y = 0, 0  # 출발위치 *
    direction = 0  #처음 출발 방향 오른쪽*

    dx = [0, 1, 0, -1]   # 우하좌상
    dy = [1, 0, -1, 0]

    for i in range(1, n * n + 1):   # *
        arr[x][y] = i
        # 다음 위치 이동
        nx = x + dx[direction]
        ny = y + dy[direction]

        # 범위안에 있어? 이미 숫자 없어?
        if 0 <= nx < n and 0 <= ny < n and arr[nx][ny] == 0: # *
            x = nx
            y = ny  # 여기로 이동하자
        else:
            # 갈수 없으면 방향을 바꿔 다시 이동하자
            direction = (direction + 1) % 4
            # direction += 1하면 인덱스 범위가 벗어나니까 상하좌우 4를 나눠서 순환할 수 있게만든다.
            x += dx[direction]
            y += dy[direction]

    print(f'#{tc}')
    for line in arr:
        print(*line)