import sys

sys.stdin = open("input.txt")

t = int(input())

for tc in range(1, t + 1):
    k, n, m = map(int, input().split())
    # k == 한번 충전으로 최대한 갈 수 있는 거리
    # n == 정류장 개수
    # m == 충전기가 있는 정류장 번호
    stations = list(map(int, input().split()))
    # 충전기가 있는 정류장 번호를 리스트로 만든다.
    start, end = 0, k  # 출발점과 도착점
    is_possible = True  # 충전소가 없는 경우 판별
    result = 0

    while end < n:
        for i in range(end, start, -1):
            # 1. 충전소가 있으면
            if i in stations:
                start = i
                end = start + k
                result += 1
                break
        else:
            is_possible = False

    print(f'#{tc} {result}')


