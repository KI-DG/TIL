def bfs(start):
    visited = [False] * (n + 1)
    # 방문했는지 안했는지 확인용 리스트를 만들어준다.
    visited[start] = True
    # 방문을 했을시 방문체크를 해준다.
    queue = [start]
    total = 0  # 결과값(감염된 컴퓨터의 개수)

    while queue:
        node = queue.pop(0)  # 현재 정점
        for next_node in graph[node]:  # 인접한 모든 정점에 대해 반복문 실행
            if not visited[next_node]:
                visited[next_node] = True
                queue.append(next_node)
                total += 1

    return total


n = int(input())  # 컴퓨터의 개수
m = int(input())  # 간선의 개수

graph = [[] for _ in range(n + 1)]

for _ in range(m):
    v1, v2 = map(int, input().split())
    graph[v1].append(v2)
    graph[v2].append(v1)

print(bfs(1))
