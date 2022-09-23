import sys

sys.stdin = open('input.txt')

t = int(input())

for tc in range(1, t + 1):
    plan = list(map(int, input().split()))
    schedule = [0] + list(map(int, input().split()))
    dp = [0] * 13

    for i in range(1, 13):
        dp[i] = dp[i-1] + min(plan)


    # answer = 0
    # print(f'#{tc} {answer}')