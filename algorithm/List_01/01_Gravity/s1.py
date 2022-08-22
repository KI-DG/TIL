import sys

sys.stdin = open("input.txt")

t = int(input())

for tc in range(t):  # 테스트 케이스를 가지고 와라
    n = int(int(input()))
    numbers = list(map(int, input().split()))

    result = 0

    for i in range(n):
        max_height = 0  # 최대 낙차값

        for j in range(i+1, n):
            if numbers[i] > numbers[j]:
                max_height += 1

        if result < max_height:
            result = max_height

    print(f'#{tc} {result}')