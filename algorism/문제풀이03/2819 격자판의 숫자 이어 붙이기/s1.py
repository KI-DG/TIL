import sys

sys.stdin = open('input.txt')

dx = [-1, 0, 1, 0]  # 상우하좌
dy = [0, 1, 0, -1]


def dfs(cnt, x, y, num):
    global answer_set
    if cnt == 7:
        answer_set.add(num)
        return

    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]

        if 0 <= nx < 4 and 0 <= ny < 4:
            next_num = num + arr[nx][ny]
            dfs(cnt + 1, nx, ny, next_num)


t = int(input())

for tc in range(1, t + 1):
    arr = [list(input().split()) for _ in range(4)]

    answer_set = set()
    for i in range(4):
        for j in range(4):
            dfs(1, i, j, arr[i][j])

    print(f'#{tc} {len(answer_set)}')