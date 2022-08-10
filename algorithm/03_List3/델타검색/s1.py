import sys

sys.stdin = open("input.TXT")

t = int(input())

for tc in range(1, t+1):
    n = int(input())
    arr = [list(map(int, input().split()))for _ in range(n)]

    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]

    total = 0

    for i in range(n):
        for j in range(n):
            for k in range(4):
                ni = i + di[k]
                nj = j + dj[k]
                if 0 <= ni < n and 0 <= nj < n:
                    result = arr[i + di[k]][j + dj[k]] - arr[i][j]
                    if result >= 0:
                        total += result
                    else:
                        total -= result


    print(f'#{tc} {total}')