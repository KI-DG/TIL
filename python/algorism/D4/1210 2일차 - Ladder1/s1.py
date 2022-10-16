import sys

sys.stdin = open("input.txt")

dx = [0, 0, -1]  # 좌 우 상
dy = [-1, 1, 0]

for _ in range(1, 11):
    tc = int(input())
    ladder = [list(map(int, input().split())) for _ in range(100)]   # 사다리를 받아온다

    for idx, number in enumerate(ladder[-1]):
        if number == 2:          # 사다리의 시작점
            x, y = 99, idx       # 사다리의 시작좌표
            break

    while x > 0:                # 출발점을 찾아야 되기때문에
        for k in range(3):      # 델타 탐색
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < 100 and 0 <= ny < 100 and ladder[nx][ny] == 1:     # 범위를 벗어나지 않고 사다리가 있으면
                ladder[x][y] = 0        # 지나온 길은 0으로처리 아니면 계속 왔다 갔다함
                x = nx                  # 다음좌표
                y = ny                  # 다음좌표

    print(f'#{tc} {y}')
