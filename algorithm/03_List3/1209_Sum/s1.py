import sys

sys.stdin = open("input.txt")

for _ in range(10):
    tc = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]
    result = 0

    for i in range(100):        # 행
        sum_line = 0
        for j in range(100):
            sum_line += arr[i][j]
        if sum_line > result:
            result = sum_line

    for j in range(100):        # 열
        sum_row = 0
        for i in range(100):
            sum_row += arr[i][j]
        if sum_row > result:
            result = sum_row

    for i in range(100):
        sum_dia = 0
        sum_dia += arr[i][i]
        if sum_dia > result:
            result = sum_dia

    for i in range(100):
        sum_back_dia = 0
        sum_back_dia += arr[99 - i][0 + i]
        if sum_back_dia > result:
            result = sum_back_dia

    print(f'#{tc} {result}')