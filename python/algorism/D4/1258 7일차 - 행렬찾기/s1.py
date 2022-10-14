import sys

sys.stdin = open('input.txt')

t = int(input())


for tc in range(1, t + 1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    result = []

    for i in range(n):
        for j in range(n):
            r, c = i, j
            r1, c1 = i, j

            r_cnt = 1
            while arr[r][c] != 0:
                nr = r + 1

                if 0 <= nr < n and arr[nr][c] != 0:
                    r_cnt += 1
                    r = nr
                else:
                    break
            c_cnt = 1
            while arr[r1][c1] != 0:
                nc = c1 + 1

                if 0 <= nc < n and arr[r1][nc] != 0:
                    c_cnt += 1
                    c1 = nc
                else:
                    result.append((r_cnt, c_cnt))
                    break

            for a in range(i, i + r_cnt):
                for b in range(j, j + c_cnt):
                    arr[a][b] = 0

    num = len(result)
    sum_result = []

    for k in range(num - 1, 0, -1):
        for d in range(0, k):
            if result[d][0] * result[d][1] > result[d + 1][0] * result[d + 1][1]:
                result[d], result[d + 1] = result[d + 1], result[d]
            elif result[d][0] * result[d][1] == result[d + 1][0] * result[d + 1][1] and result[d][0] > result[d + 1][0]:
                result[d], result[d + 1] = result[d + 1], result[d]

    print(f'#{tc} {num}', end='')
    for i in result:
        print('', *i, end='')
    print()
