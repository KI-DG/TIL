import sys

sys.stdin = open("input.txt")

t = int(input())

for tc in range(1, t + 1):
    n = int(input())
    # 파스칼의 삼각형 값을 담을 배열 생성
    borad = [[0] * (i + 1) for i in range(n)]

    for i in range(n):      # 파스칼의 삼각형을 구하는 공식
        for j in range(i + 1):
            borad[i][0] = borad[i][i] = 1       # 첫번쨰랑 끝에만 1을 추가
            if borad[i][j] != 1:        # 가운데는 위의 값을 더한 값
                borad[i][j] = borad[i - 1][j] + borad[i - 1][j - 1]

    print(f'#{tc}')
    for i in range(n):
        print(*borad[i])



