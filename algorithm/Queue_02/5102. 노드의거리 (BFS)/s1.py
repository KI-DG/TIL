import sys

sys.stdin = open('input')


def bfs(s, f):
    visited = [False] * (v + 1)   # 방문자 리스트를 만든다.
    queue = [s]   # queue 리스트 생성

    while queue:
        node = queue.pop(0)  # 현재 정점
        for next_s in graph[node]:  # 인접 정점으로 이동
            if not visited[next_s]:   # 방문을 안했으면
                visited[next_s] = visited[node] + 1
                if next_s == f:
                    return visited[next_s]
                queue.append(next_s)

    return 0


t = int(input())

for tc in range(1, t + 1):
    v, e = map(int, input().split())
    graph = [[] for _ in range(v + 1)]  # 인접 리스트를 만든다.

    for _ in range(1, e + 1):
        v1, v2 = map(int, input().split())
        graph[v1].append(v2)
        graph[v2].append(v1)

    start, end = map(int, input().split())

    print(f'#{tc}', bfs(start, end))
