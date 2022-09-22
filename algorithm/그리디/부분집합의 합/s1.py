import sys

sys.stdin = open("input")


def dfs(n, sm, cnt):
    global ans
    if n == N:
        if sm == k and cnt == CNT:
            ans += 1
        return
    dfs(n+1, sm + lst[n], cnt + 1)   # 사용하는 경우
    dfs(n+1, sm, cnt)                # 사용하지 않는 경우


t = int(input())

for tc in range(1, t + 1):
    CNT, k = map(int, input().split())
    lst = [n for n in range(1, 13)]
    N = len(lst)

    ans = 0
    dfs(0, 0, 0)

    print(f'#{tc} {ans}')