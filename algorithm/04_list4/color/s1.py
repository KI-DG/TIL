import sys

sys.stdin = open("input")

t = int(input())

for tc in range(1, t+1):
    n = int(input())
    arr = [[0 for _ in range(11)] for _ in range(11)]
    # [[0]*10]*10 이렇게 쓰면 안되지만 이런 모양을 만든다.
    cnt = 0 # 겹치는 부분을 카운트한다.
    for i in range(n):
        r1, c1, r2, c2, color = map(int, input().split())
        # 반복을 돌려서 범위랑 색을 구별
        for x in range(r1, r2+1):
            # 행의 색칠하는 부분을 찾는다
            for y in range(c1, c2+1):
                # 열의 색칠하는 부분을 찾는다
                arr[x][y] += color
                # 색깔을 찾는다
                if arr[x][y] == 3:  # 겹치는 부분을 찾는다 빨강은 1 파랑은 2 합치면 3
                    cnt += 1

    print(f"#{tc} {cnt}")