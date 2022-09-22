import sys

sys.stdin = open('input.txt')

t = int(input())

for tc in range(1, t + 1):
    n, k = map(int, input().split())
    coins = []
    for i in range(n):
        coins.append(int(input()))
    # coins = [int(input()) for _ in range(n)]
    result = 0

    for i in range(n - 1, -1, -1):
        result += k // coins[i]
        k %= coins[i]

    print(result)