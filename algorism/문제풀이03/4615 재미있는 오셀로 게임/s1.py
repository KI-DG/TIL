import sys

sys.stdin = open("input.txt")

dx = [-1, 0, 1, 0, 1, 1, -1, -1]  # 대각선까지 봐야되기 때문에
dy = [0, 1, 0, -1, 1, -1, 1, -1]


t = int(input())

for tc in range(1, t + 1):
    n, m = map(int, input().split())
    arr = [[0] * n for _ in range(n)]

    center1 = n // 2 - 1
    center2 = n // 2

    arr[center1][center1] = 2
    arr[center1][center2] = 1
    arr[center2][center1] = 1
    arr[center2][center2] = 2

    for i in range(m):
        x, y, color = map(int, input().split())
        x -= 1
        y -= 1
        arr[x][y] = color

        for k in range(8):
            i = 1
            move_x = x + dx[k] * i
            move_y = y + dy[k] * i

            while 0 <= move_x < n and 0 <= move_y < n and arr[move_x][move_y] == 3 - color:
                i += 1
                move_x = x + dx[k] * i
                move_y = y + dy[k] * i

            if 0 <= move_x < n and 0 <= move_y < n and arr[move_x][move_y] == color:
                for j in range(1, i):
                    arr[x + dx[k] * j][y + dy[k] * j] = color

    cnt_stone = [0, 0]
    for a in range(n):
        for b in range(n):
            if arr[a][b] == 1:
                cnt_stone[0] += 1
            elif arr[a][b] == 2:
                cnt_stone[1] += 1

    print(f'#{tc}', *cnt_stone)