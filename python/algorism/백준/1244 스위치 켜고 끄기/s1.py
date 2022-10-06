import sys

sys.stdin = open("input.txt")

swi = int(input())
swi_arr = list(map(int, input().split()))
n = int(input())

for i in range(n):
    m, k = map(int, input().split())

    if m == 1:                              # 남자일때
        for j in range(k, swi + 1):
            if j % k == 0:                  # k의 배수일때
                if swi_arr[j - 1] == 0:     # 0이면 1로 1이면 0으로 바꿔준다
                    swi_arr[j - 1] = 1
                else:
                    swi_arr[j - 1] = 0
    else:                                   # 여자일떄
        num = k - 1                         # 인덱스 편의를 위해 -1 을 빼준다
        if swi_arr[num] == 0:               # 자기 자신은 0이면 1로 1이면 0으로 바꿔준다
            swi_arr[num] = 1
        else:
            swi_arr[num] = 0
        for j in range(1, swi // 2):        # 좌 우 대칭이이거나 범위를 안벗어나면
            if 0 <= num - j and num + j <= swi - 1 and swi_arr[num - j] == swi_arr[num + j]:
                if swi_arr[num - j] == 0:
                    swi_arr[num - j], swi_arr[num + j] = 1, 1
                else:
                    swi_arr[num - j], swi_arr[num + j] = 0, 0

while swi_arr:
    print(*swi_arr[:20])
    swi_arr = swi_arr[20:]
