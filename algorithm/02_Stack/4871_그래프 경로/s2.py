import sys

sys.stdin = open('input.txt')


def dfs(s):
    visited[s] = True

    for next_s in graph[s]:
        if not visited[next_s]:
            dfs(next_s)


t = int(input())

for tc in range(1, t+1):
    v, e = map(int, input().split())    # 정점 개수, 간선 개수
    graph = [[] for _ in range(v + 1)]
    visited = [False] * (v + 1)

    for _ in range(1, e + 1):
        v1, v2 = map(int, input().split())
        graph[v1].append(v2)
    start, end = map(int, input().split())      # 출발과 도착 지점

    dfs(start)
    answer = 1
    if not visited[end]:
        answer = 0

    print(f"#{tc} {answer}")