import sys

sys.stdin = open('input')

dx = [-1, 1, 0, -1, 1]
dy = [0, 0, 1, 1, 1]


def omok(arr):
    global answer
    for i in range(n):
        for j in range(n):
            if arr[i][j] == 'o':
                for k in range(5):
                    nx = i + dx[k]
                    ny = j + dy[k]

                    while 0 <= nx < n and 0 <= ny < n and arr[nx][ny] == 'o':
                        arr[nx][ny]

    return answer


t = int(input())

for tc in range(1, t + 1):
    n = int(input())
    board = [list(input()) for _ in range(n)]
    answer = 'NO'
    omok(board)

    print(f'#{tc} {answer}')