import sys

sys.stdin = open('input')


def dfs(s):
    visited[s] = True

    for next_s in graph[s]:
        if not visited[next_s]:
            dfs(next_s)


for tc in range(1, 11):
    t, e = map(int, input().split())    # test 개수, 간선 개수
    graph = [[] for _ in range(100)]
    visited = [False] * 100

    data = list(map(int, input().split()))
    start, end = 0, 99      # 출발과 도착 지점

    for i in range(e):      # 인접 리스트를 만들어라
        graph[data[i*2]].append(data[i*2+1])

    dfs(start)
    answer = 1
    if not visited[end]:
        answer = 0

    print(f"#{tc} {answer}")