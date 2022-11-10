import sys

sys.stdin = open('input')

t = int(input())

for tc in range(1, t + 1):
    n = int(input())   # 농장의 크기
    farm = [list(map(int, input())) for _ in range(n)]
    farm_sum = 0

    s, e = n // 2, n // 2
    for i in range(n):
        for j in range(s, e + 1):
            farm_sum += farm[i][j]
        if i < n // 2:
            s -= 1
            e += 1
        else:
            s += 1
            e -= 1
    print(f"#{tc} {farm_sum}")

