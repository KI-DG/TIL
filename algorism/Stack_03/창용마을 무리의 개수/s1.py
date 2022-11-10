import sys

sys.stdin = open('input')


def dfs(x):
    global total
    visited[x] = True
    total += 1

    for next_s in borad[x]:
        if not visited[next_s]:
            dfs(next_s)


t = int(input())

for tc in range(1, t + 1):
    n, m = map(int, input().split())
    # n == 창용마을에 사는 사람의 수 m == 서로를 알고 있는 사람의 관계 수
    borad = [[] for _ in range(n + 1)]
    visited = [False] * (n + 1)
    result = []

    for _ in range(1, m + 1):
        a, b = map(int, input().split())
        borad[a].append(b)
        borad[b].append(a)

    for i in range(1, n + 1):
        if not visited[i]:
            total = 0
            dfs(i)
            result.append(total)

    print(f'#{tc} {len(result)}')

