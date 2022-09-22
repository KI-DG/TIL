import sys

sys.stdin = open("input.txt")


def dfs(num, sum_num):
    global ans
    # 최소값이면 가지치기를 생각해라 (가지치기는 제일 마지막에)

    if ans <= sum_num:
        return

    if num == n:
        if ans > sum_num:
            ans = sum_num
        return

    for j in range(n):
        if not v[j]:
            v[j] = 1
            dfs(num + 1, sum_num + arr[num][j])
            v[j] = 0


t = int(input())

for tc in range(1, t + 1):
    n = int(input())

    arr = [list(map(int, input().split())) for _ in range(n)]
    v = [0] * n
    ans = 10 * n  # 최소값을 구할경우, 초기값은 최대치

    dfs(0, 0)

    print(f'#{tc} {ans}')