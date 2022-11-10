import sys

sys.stdin = open("input.TXT")

t = int(input())

for tc in range(1, t + 1):
    arr = list(map(int, input().split()))

    n = len(arr)  # 원소의 개수

    result = 0  # True 인지 False 인지 확인하기위해

    for i in range(1, 1 << n):  # 부분집합의 개수
        sum_value = 0  # 부분집합의 합
        for j in range(n):
            if i & (1 << j):
                sum_value += arr[j]

        if sum_value == 0:
            result += 1
            break

    print(f'#{tc} {result}')

