import sys
from heapq import heappop, heappush
sys.stdin = open('input.txt')

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]


def dijkstra(row, col):
    heap = [(0, row, col)]
    distance[row][col] = 0         # 초기값을 가진다

    while heap:
        min_dist, row, col = heappop(heap)     # 첫번째 값을 삭제해준다
        if distance[row][col] < min_dist:      # 가지치기 값보다 최소값이 더 크지 않으면 진행
            continue
        for i in range(4):                     # 델타 검색을 통해 주위를 살펴준다
            nx = dx[i] + row
            ny = dy[i] + col
            if 0 <= nx < n and 0 <= ny < n:              # 범위내에 있고
                if arr[nx][ny] > arr[row][col]:          # 다음값이 지금 값보다 크면
                    nd = min_dist + 1 + arr[nx][ny] - arr[row][col]   # 기본 이동할때 1 움직여주고 추가로 높이 만큼 더해준다
                else:
                    nd = min_dist + 1                    # 아니면 그냥 1만 추가

                if nd < distance[nx][ny]:
                    distance[nx][ny] = nd          # 값을 초기화
                    heappush(heap, (nd, nx, ny))   # 최소값을 알아서 찾아준다


t = int(input())
INF = 99999999
for tc in range(1, t + 1):
    n = int(input())  # n의 크기
    arr = [list(map(int, input().split())) for _ in range(n)]
    distance = [([INF] * n) for _ in range(n)]

    dijkstra(0, 0)

# 1. 델타검색을 해서 주위에 값중 최소값을 찾는다
# 2. 만약 같은 첫번째 값과 같지 않으면 차이값을 빼서 더해준다
    print(f'#{tc} {distance[-1][-1]}')

# (위로가거나 밑으로 내려가는 경우는 없음으로 우 하만 확인) -- 있음
