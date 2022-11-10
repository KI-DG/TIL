import sys

sys.stdin = open('input.txt')
# 델타 검색??
# dx = [-1, 0, 1, 0]
# dy = [0, 1, 0, -1]


def home_crime(k):
    global cnt, max_cnt
    while True:
        if break_even_point < 0:
            if max_cnt < cnt:
                max_cnt = cnt
            break
        # 손해를 보지 않을 때까지 계속 확장 (종료조건)
        s, e = k // 2, k // 2
        for a in range(k):                           # 다이아몬드 형 반복문
            for b in range(s, e + 1):
                if 0 < a <= n and 0 < b <= n:
                    if house_map == 1:
                        cnt += 1                        # 집이 있다면 집을 더해준다
                if a < k // 2:
                    s -= 1
                    e += 1
                else:
                    s += 1
                    e -= 1
        k += 1




t = int(input())

for tc in range(1, t + 1):
    n, m = map(int, input().split())            # n = 지도의 크기, m은 낼수 있는돈
    max_cnt = 0                                 # 집의 개수 최대값
    cnt = 1                                     # 집의 개수
    k = 1                                       # 홈방범 범위 초기값
    manage_money = 2 * k * (k - 1) + 1          # 운영비용
    break_even_point = cnt * m - manage_money   # 손익분기점
    house_map = [list(map(int, input().split())) for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if house_map[i][j] == 1:
                home_crime(k)
    print(f'#{tc} {max_cnt}')




