import sys

sys.stdin = open("input.txt")

for _ in range(1, 11):
    tc = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]

    answer = 0
    for i in range(100):
        row_sum = 0
        col_sum = 0
        dia1_sum = 0
        dia2_sum = 0
        for j in range(100):
            row_sum += arr[i][j]

            if row_sum > answer:
                answer = row_sum

            col_sum += arr[j][i]

            if col_sum > answer:
                answer = col_sum

            if i == j:
                dia1_sum += arr[i][j]

                if dia1_sum > answer:
                    answer = dia1_sum

            dia2_sum = arr[i][99 - i]

            if dia2_sum > answer:
                answer = dia2_sum

    print(f'#{tc} {answer}')