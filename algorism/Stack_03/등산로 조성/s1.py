import sys

sys.stdin = open('input')

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

t = int(input())

for tc in range(1, t + 1):
    n, k = map(int, input().split())
    # n == 지도 크기 k == 최대 공사 가능 깊이
    board = [list(map(int, input().split())) for _ in range(n)]
    visited = [[False] * n for _ in range(n)]
    result = []

    # 가장 높은 봉우리에서 시작

    # 낮은 지형, 높은 지형에서 가로 세로 방향으로 연결이 되어야 한다. #대각선 방향의 연결은 불가능
    # 긴 등산로를 만들기 위해 딱 한 곳을 정해서 최대 K 깊이만큼 지형을 깎는 공사를 할 수 있다.


    print(f'#{tc} {result}')