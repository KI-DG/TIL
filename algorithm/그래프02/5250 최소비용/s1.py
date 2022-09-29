import sys
from heapq import heappop, heappush
sys.stdin = open('input.txt')

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]


def dijkstra(row, col):
    distance[row][col] = 0
    heap = [(0, row, col)]

    while heap:
        min_dist, min_node[row][col] = heappop(heap)


t = int(input())
INF = 99999999
for tc in range(1, t + 1):
    n = int(input())  # n의 크기
    arr = [list(map(int, input().split())) for _ in range(n)]
    distance = [INF] * (n + 1)

    dijkstra()

# 1. 델타검색을 해서 주위에 값중 최소값을 찾는다(위로가거나 밑으로 내려가는 경우는 없음으로 우 하만 확인)
# 2. 만약 같은 첫번째 값과 같지 않으면 차이값을 빼서 더해준다









    answer = 0
    print(f'#{tc} {answer}')