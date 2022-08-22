import sys

sys.stdin = open("input.txt")

t = int(input())

for tc in range(1, t + 1):
    n = int(input())
    ai = list(map(int, input().split()))

    result_a = []

    for i in range(n - 1, -1, -1):  # 버블 정렬로 오름차순을 만들어준다.
        for j in range(0, i):
            if ai[j] > ai[j + 1]:
                ai[j], ai[j + 1] = ai[j + 1], ai[j]

    for x in range(10):         # *
        if x % 2:
            result_a.append(ai[x//2])
        # 인덱스 홀수인 상태
        else:
            result_a.append(ai[-1 * (x // 2) - 1])
        # 인덱스 짝수인 상태

    print(f"#{tc}", *result_a)



