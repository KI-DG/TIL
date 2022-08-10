#길이에 관한건 0으로 초기화해라

import sys

sys.stdin = open("input.txt")

t = int(input())

for tc in range(1,t+1):
    n = int(input())
    arr = list(map(int, input()))

    maxV = 0
    cnt = 0
    for i in range(n):
        if arr[i] == 1:
            cnt += 1
            if maxV < cnt:
                maxV = cnt
        else:
            cnt = 0

    print(f'#{tc} {maxV}')
    # for i in range(n):
    #     arr[i] = arr[i-1]*arr[i] + arr[i]
    #