import sys

sys.stdin = open("input.txt")

t = int(input())

for tc in range(1, t + 1):
    n, k = map(int, input().split())

    a = [int(i) for i in range(1, 13)]  # a집합의 수 *a 집합의 설정을 잘못하였다.

    result = 0

    for i in range(1 << len(a)):  # 부분집합의 개수
        subset = []  # 부분집합을 넣어놓는 리스트의 개수
        for j in range(len(a)):
            if i & (1 << j):  # 부분집합을 넣는방법
                subset.append(a[j])
        if len(subset) == n and sum(subset) == k:
            result += 1

    print(f"#{tc} {result}")


