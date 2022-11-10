import sys

sys.stdin = open('input')

for tc in range(1, 11):
    t = int(input())
    n = 100
    woo = [input() for _ in range(n)]
    woo_woo = [["" * n for _ in range(n)] for _ in range(n)]
    young = ''

    for i in range(n):
        for j in range(n):
            woo_woo[i][j] = woo[j][i]

    for m in range(100, 2, -1):
        for i in range(n):
            for j in range(n - m + 1):
                # 가로 회문 구하기
                if woo[i][j:j + m] == woo[i][j:j + m][::-1]:
                    if m > len(young):
                        young = woo[i][j:j + m]

                # 세로 회문 구하기
                if woo_woo[i][j:j + m] == woo_woo[i][j:j + m][::-1] and m > len(young):
                    young = woo_woo[i][j:j + m]

        if young:
            break

    print(f'#{tc} {len(young)}')
