import sys

sys.stdin = open('input.txt')

t = int(input())
for tc in range(1, t + 1):
    n = int(input())
    dp = [[1] * (i + 1) for i in range(n)] # DP 테이블 초기화

		# 각 행의 열 맨 앞과 뒤는 1로 초기화되어 있어 변경 필요 X
    for i in range(2, n): # 값 변경이 필요한 DP 테이블의 행과 열에 대해
        for j in range(1, i):
            # 현재 행의 열 값 = 바로 위 행의 바로 왼쪽 열 요소값 + 바로 위 행의 동일 열 요소값
            dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]

    print(f'#{tc}')
    for i in range(n):
        print(*dp[i])