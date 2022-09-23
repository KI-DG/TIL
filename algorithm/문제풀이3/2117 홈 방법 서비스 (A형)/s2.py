import sys

sys.stdin = open('input.txt')
# 이게 아니다!!!!!!!!!!!
# dx = [-1, 0, 1, 0]
# dy = [0, 1, 0, -1]


def home_dfs(k, cnt, x, y):
    global max_cnt
    while True:
        manage_money = 2 * k * (k - 1) + 1              # 운영비용
        break_even_point = cnt * m - manage_money      # 손익분기점
        if break_even_point < 0:
            if max_cnt < cnt:
                max_cnt = cnt
            break

        cnt = 1
        s, e = (k + 2) // 2, (k + 2) // 2
        for a in range(k + 2):                          # 다이아몬드 형 반복문
            for b in range(s, e + 1):
                if house_map[a][b] == 1:
                    cnt += 1  # 집이 있다면 집을 더해준다
                # for w in range(4):
                #     nx = x + dx[w]
                #     ny = y + dy[w]
                #     if 0 <= nx < n and 0 <= ny < n:
                #         if house_map[nx][ny] == 1:
                #             cnt += 1                    # 집이 있다면 집을 더해준다
                if a < (k + 2) // 2:
                    s -= 1
                    e += 1
                else:
                    s += 1
                    e -= 1
                if cnt == 1:
                    break
        k += 1


        # for w in range(4):
        #     nx = x + dx[w]
        #     ny = y + dy[w]
        #
        #     if 0 <= nx <= n and 0 <= ny <= n:
        #         if house_map[nx][ny] == 1:
        #             home_dfs(nx, ny, cnt + 1)


t = int(input())
for tc in range(1, t + 1):
    n, m = map(int, input().split())            # n = 지도의 크기, m은 낼수 있는돈
    max_cnt = 0                                 # 집의 개수 최대값
    k = 1                                       # 홈방범 범위 초기값
    home = 1
    house_map = [list(map(int, input().split())) for _ in range(n)]   # 지도
    for i in range(n):
        for j in range(n):
            if house_map[i][j] == 1:
                home_dfs(k, home, i, j)

    print(f'#{tc} {max_cnt}')
