import sys

sys.stdin = open('input')

t = int(input())

for tc in range(1, t + 1):
    n = int(input())
    data = list(map(int, input().split()))
    result = 0

    for i in range(1, n):
        if data[i - 1] <= data[i] != data[-1]:
            if result <= data[i - 1] * data[i]:
                result = data[i - 1] * data[i]

    print(f"#{tc} {result}")