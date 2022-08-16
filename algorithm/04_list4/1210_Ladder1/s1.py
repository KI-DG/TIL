import sys

sys.stdin = open('input.txt')

dx = [0, 0, -1]     # 좌 우 상
dy = [-1, 1, 0]

for _ in range(10):
    t = int(input())
    ladder = [input().split() for _ in range(100)]

    # 1. 마지막 줄에서 x 지점 찾기
    for i, number in enumerate(ladder[-1]):
        if number == 2:
            x, y = 99, i
            break
    # 2. 사다리 타고 올라가기
    while x > 0:
        for i in range(3):
            nx = x + dx[i]
            ny = y + dy[i]

            # 범위 확인
            if 0 <= nx < 100 and 0 <= ny < 100 and ladder[nx][ny] == '1':
                ladder[x][y] = '0'  # 0으로 안바꾸면 옆으로 가지를 못한다.
                x, y = nx, ny

        print(f"#{t} {y}")
