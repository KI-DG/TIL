import sys

sys.stdin = open("input")

t = int(input())

for tc in range(1, t + 1):
    n = int(input())  # 노선의 수
    stop = [0] * 1001  # 1~1000번 정류장

    for _ in range(n):
        bus, a, b = (map(int, input().split()))
        stop[a] += 1  # a, b에는 항상 정차
        stop[b] += 1
        if bus == 1:
            for i in range(a+1, b):
                stop[i] += 1
        elif bus == 2:  # 급행은 a가 짝수면 모든 짝수정류장에 도착
            # if a % 2 == 0:
            #     for i in range(a+1, b):
            #         if i % 2 == 0:
            #             stop[i] += 1
            # else:
            #     for i in range(a+1, b):
            #         if i % 2 == 1:
            #             stop[i] += 1
            for i in range(a + 2, b, 2):
                stop[i] += 1
        else:
            if a % 2 == 0:
                for i in range(a + 1, b):
                    if i % 4 == 0:
                        stop[i] += 1
            else:
                for i in range(a + 1, b):
                    if i % 3 == 0 and i % 10 != 0:
                        stop[i] += 1

    print(f'#{tc} {max(stop)}')