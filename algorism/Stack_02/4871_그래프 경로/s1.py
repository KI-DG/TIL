import sys

sys.stdin = open("input")


def dfs(s):
    visited[s] = True

    while True:
        for next_s in graph[s]:
            if not visited[next_s]:
                stack.append(s)
                s = next_s
                visited[s] = True
                break
        else:
            if stack:
                s = stack.pop()
            else:
                break


t = int(input())

for tc in range(1, t+1):
    v, e = map(int, input().split())    # 정점 개수, 간선 개수
    graph = [[] for _ in range(v + 1)]      # 인접 리스트를 만든다.
    visited = [False] * (v + 1)     # 방문 했는지 안했는지 알아보는 리스트
    stack = []
    for _ in range(1, e + 1):       # 인접리스트에 값을 채워준다.
        v1, v2 = map(int, input().split())
        graph[v1].append(v2)

    start, end = map(int, input().split())      # 출발과 도착 지점
    dfs(start)

    answer = 1
    if not visited[end]:
        answer = 0

    print(f"#{tc} {answer}")


