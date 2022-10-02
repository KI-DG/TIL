import sys

sys.stdin = open("input.txt")

t = int(input())

for tc in range(1, t + 1):
    n, m = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]

    answer = []
    for i in range(n - m + 1):
        for j in range(n - m + 1):
            kill = 0
            for x in range(i, i + m):
                for y in range(j, j + m):
                    kill += arr[x][y]
            answer.append(kill)
    ans = max(answer)
    print(f'#{tc} {ans}')