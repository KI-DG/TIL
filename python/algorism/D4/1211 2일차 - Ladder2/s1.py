import sys

sys.stdin = open("input.txt")

dx = [0, 0, 1]      # 좌 우 하
dy = [-1, 1, 0]

for _ in range(1, 10 + 1):
    t = int(input())
    ladder = [list(map(int, input().split())) for _ in range(100)]      # 사다리를 만들기

    min_load = 10000             # 최소값을 만들어주기 위해
    j = 0
    for i in range(100):
        if ladder[0][i] == 1:       # 출발점 찾기
            x, y = 0, i             # 출발점 좌표
            cnt = 0                     # 최단거리를 세기위한 변수
            visited = [[0] * 100 for _ in range(100)]

            while x < 99:
                for k in range(3):      # 델타 탐색
                    nx = x + dx[k]
                    ny = y + dy[k]

                    if 0 <= nx < 100 and 0 <= ny < 100 and ladder[nx][ny] == 1 and visited[nx][ny] == 0:     # 범위내에 있으면서 사다리이면
                        x, y = nx, ny                  # 다음좌표로 이동
                        visited[nx][ny] = 1        # 사다리는 0으로 만들어준다
                        cnt += 1                # 거리 +1
                # if min_load < cnt:
                #     break
            if min_load > cnt:
                min_load = cnt
                j = i
    print(f'#{t} {j}')
