from heapq import heappush, heappop
import sys

sys.stdin = open('input.txt')

INF = int(1e9)          # 무한대


def dijkstra(start):
    distance[start] = 0
    heap = [(0, start)]     # 힙선언

    while heap:
        # 1. 최단 거리가 가장 짧은 정점을 선택
        min_dist, node = heappop(heap)
        # 2. 이미 최단 거리로 기록되어 있는 값보다 높은 경우 무시
        if min_dist > distance[node]:
            continue
        # 3. 해당 정점에 인접한 정점에 대해 최단 거리 갱신
        for next_node, dist in road_list[node]:             # road_list == [[(1, 1), (2, 6)], [(2, 1)], []]
            new_dist = dist + min_dist
            if new_dist < distance[next_node]:
                distance[next_node] = new_dist
                heappush(heap, (new_dist, next_node))


t = int(input())

for tc in range(1, t + 1):
    city, road = map(int, input().split())    # 마지막 지점, 도로의 개수
    road_list = [[] for _ in range(city + 1)]   # 연결된 도로와 구간 거리를 저장할 빈 리스트
    distance = [INF] * (city + 1)

    for i in range(road):                     # 연결된 도로의 리스트를 받아온다
        s, e, w = map(int, input().split())
        road_list[s].append((e, w))           # 빈 리스트에 추가
    dijkstra(0)
    print(f'#{tc} {distance[e]}')