import sys

sys.stdin = open("input")

t = int(input())

for tc in range(1, t + 1):
    n, m = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]

    maxV = 0
    for i in range(n):
        cnt = 0
        for j in range(m):
            if arr[i][j]:
                cnt += 1
                if maxV < cnt:
                    maxV = cnt
            else:
                cnt = 0

    for j in range(m):
        cnt = 0
        for i in range(n):
            if arr[i][j]:
                cnt += 1
                if maxV < cnt:
                    maxV = cnt
            else:
                cnt = 0

    print(f'#{tc} {maxV}')

