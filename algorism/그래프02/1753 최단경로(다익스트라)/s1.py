import sys
from heapq import heappush, heappop

sys.stdin = open('input.txt')
input = sys.stdin.readline


def dijkstra(start):
    distance[start] = 0
    heap = [(0, start)]  # 힙 선언 [(비용, 정점)]

    while heap:
        # 1. 최단 거리가 가장 짧은 정점을 선택
        min_dist, min_node = heappop(heap)

        # 2. 이미 최단 거리로 기록되어 있는 값보다 높은 경우 무시
        if min_dist > distance[min_node]:
            continue

        # 3. 해당 정점에 인접한 정점에 대해 최단 거리 갱신
        for next_node, dist in graph[min_node]:
            new_dist = min_dist + dist
            if new_dist < distance[next_node]:
                distance[next_node] = new_dist
                heappush(heap, (new_dist, next_node))


# def dijkstra(node):
#     visited = [False] * (v + 1)
#     visited[node] = True
#     distance[node] = 0
#
#     for e, w in graph[node]:
#         distance[e] = w
#
#     for _ in range(v - 1):
#         min_dist = INF
#         for i in range(1, v + 1):
#             if not visited[i] and min_dist > distance[i]:
#                 min_node = i
#                 min_dist = distance[i]
#
#         visited[min_node] = True
#
#         for next_node, dist in graph[min_node]:
#             new_dist = distance[min_node] + dist
#             if new_dist < distance[next_node]:
#                 distance[next_node] = new_dist


v, m = map(int, input().split())  # 정점의 개수, 간선의 개수
k = int(input())   # 시작지점
graph = [[] for _ in range(v + 1)]   # 인접리스트 만들어주기
INF = 1000 * 1000                    # 최대값을 생성
distance = [INF] * (v + 1)           # 최소값의 거리 만들어줘야된다

for _ in range(m):
    start, end, weight = map(int, input().split())
    graph[start].append((end, weight))

dijkstra(k)

for j in range(1, v + 1):
    if distance[j] == INF:
        distance[j] = 'INF'
    print(distance[j])
