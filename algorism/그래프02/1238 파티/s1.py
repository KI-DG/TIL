from heapq import heappush, heappop
import sys

sys.stdin = open('input.txt')
INF = int(1e9)          # 무한대


def dijkstra(start):
    distance[start] = 0
    heap = [(0, start)]

    while heap:
        min_dist, min_node = heappop(heap)

        if min_dist > distance[min_node]:
            continue

        for next_node, dist in graph[min_node]:
            new_dist = min_dist + dist
            if new_dist < distance[next_node]:
                distance[next_node] = new_dist
                heappush(heap, (new_dist, next_node))


n, m, x = map(int, input().split())
graph = [[] for _ in range(n + 1)]    # 인접 리스트를 만들 빈리스트 작성

for _ in range(m):
    s, e, t = map(int, input().split())
    graph[s].append((e, t))           # 인접 리스트 작성

answer = [0] * (n + 1)

for i in range(1, n + 1):
    distance = [INF] * (n + 1)
    dijkstra(i)
    if i == x:
        answer = [x + y for x, y in zip(answer, distance)]
    else:
        answer[i] += distance[x]

print(max(answer[1:]))
