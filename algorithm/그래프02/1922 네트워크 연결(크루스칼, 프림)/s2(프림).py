import sys

sys.stdin = open('input.txt')


def prim(s):
    visited = [False] * (n + 1)
    distance = [inf] * (n + 1)
    distance[s] = 0
    costs = 0

    for _ in range(n):
        min_dist = inf

        for i, dist in enumerate(distance):
            if not visited[i] and dist < min_dist:
                min_node = i
                min_dist = dist

        visited[min_node] = True
        costs += min_dist

        for next_node, dist in graph[min_node]:
            if not visited[next_node] and dist < distance[next_node]:
                distance[next_node] = dist

    return costs


n = int(input())    # 컴퓨터의 수
m = int(input())    # 연결할 수 있는 선의 수
graph = [[] for _ in range(n + 1)]
inf = 1000*1000
for _ in range(m):
    start, end, cost = map(int, input().split())
    graph[start].append((end, cost))
    graph[end].append((start, cost))

print(prim(1))
