import sys

sys.stdin = open('input')

t = int(input())

for tc in range(1, t + 1):
    n, m = map(int, input().split())
    data = list(map(int, input().split()))

    print(data)