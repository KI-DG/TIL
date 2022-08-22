import sys

sys.stdin = open('input')

t = int(input())

for tc in range(1, t + 1):
    n, m = map(int, input().split())

    # 가로와 세로 모두 찾아야 됨
    # 가로에 담긴 리스트 먼저 만들고
    woo = [input() for _ in range(n)]
    woo_woo = [["" * n for _ in range(n)] for _ in range(n)]

    result = ""
    for i in range(n):  # 세로형 추출
        for j in range(n):
            woo_woo[i][j] = woo[j][i]

    for i in range(n):  # 가로형 추출
        for j in range(n - m + 1):
            if woo[i][j:j+m] == woo[i][j:j+m][::-1]:
                result += woo[i][j:j+m]
            if woo_woo[i][j:j+m] == woo_woo[i][j:j+m][::-1]:
                result += "".join(woo_woo[i][j:j+m])

    print(f'#{tc} {result}')


    # for i in range(n):
    #     for j in range(n):
    #         woo_woo[i] += woo[j][i]
    #
    # result = 0
    #
    # for i in range(n):
    #     half = m // 2
    #     for j in range(n - m + 1):
    #         woo_i = woo[i][j: j + m]
    #         if woo_i[:half] == woo_i[-half:][::-1]:
    #             print(f'#{tc} {woo_i}')
    #         woo_woo_i = woo_woo[i][j: j + m]
    #         if woo_woo_i[:half] == woo_woo_i[-half:][::-1]:
    #             print(f'#{tc} {woo_woo_i}')
        # 세로에 들어갈 리스트 하나 만들고

        # 그것을 반복문을 돌려 똑같은지 아닌지 판단

