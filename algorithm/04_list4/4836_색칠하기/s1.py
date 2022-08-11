import sys

sys.stdin = open('input.txt')

t = int(input())

for tc in range(1, t + 1):
    n = int(input())

    arr = [[0]*10 for _ in range(10)]  # [0]인 10 * 10 영역을 만든다.

    count = 0  # 겹치는 부분을 세준다
    for i in range(n):
        r1, c1, r2, c2, color = map(int, input().split())

        for x in range(r1, r2 + 1):  # 행의 값을 칠해준다.
            for y in range(c1, c2 + 1):  # 열의 값을 칠해준다
                arr[x][y] += color  # 색상을 더해준다. 
                if arr[x][y] == 3:  # 보라색은 3이다.
                    count += 1  # 보라색이면 +1 카운트해줘라

    print(f"#{tc} {count}")


