# DP
import sys

sys.stdin = open('input.txt')

t = int(input())

for tc in range(1, t + 1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]

    memo = [[0] * n for _ in range(n)]   # 값을 저장할 리스트를 만들어준다

    for i in range(n):
        for j in range(n):
            # 1번 원래 리스트 값을 더한다
            memo[i][j] += arr[i][j]
            # 2번 위, 왼쪽을 더해서 최소합으로 갱신
            if i == 0 and j == 0:
                continue

            if i == 0:
                memo[i][j] += memo[i][j-1]

            elif j == 0:
                memo[i][j] += memo[i-1][j]

            else:
                memo[i][j] += min(memo[i-1][j], memo[i][j-1])

    print(f'#{tc} {memo[n-1][n-1]}')