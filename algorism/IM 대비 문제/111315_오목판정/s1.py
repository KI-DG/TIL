import sys

sys.stdin = open('input')

dx = [-1, 0, 1, 0, -1, -1, 1, 1]
dy = [0, -1, 0, 1, 1, -1, 1, -1]


def omok(arr):
    global answer
    for i in range(n):
        cnt = 0
        for j in range(n):
            if arr[i][j] == 'o':
                for k in range(8):
                    x = 1
                    nx = i + dx[k] * x
                    ny = j + dy[k] * x
                    while 0 <= nx < n and 0 <= ny < n and arr[nx][ny] == 'o':
                        x += 1
                        nx = i + dx[k] * x
                        ny = j + dy[k] * x
                        if x >= 5:
                            answer = 'YES'
                            break


t = int(input())

for tc in range(1, t + 1):
    n = int(input())
    board = [list(input()) for _ in range(n)]
    answer = 'NO'
    omok(board)

    print(f'#{tc} {answer}')