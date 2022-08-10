import sys

sys.stdin = open("input")

t = int(input())

for tc in range(1, t + 1):
    n, k = map(int, input().split())
    # n == 부분집합 원소 개수, k == 부분집합의 합
    num = [int(i) for i in range(1, 13)] # A 집합

    cnt = 0

    for i in range(1 << len(num)):  # A 전체 부분집합의 개수
        lst = []    #
        for j in range(len(num)):
            if i & (1 << j):
                lst.append(num[j])
        if len(lst) == n and sum(lst) == k:
            cnt += 1

    print(f"# {tc} {cnt}")
