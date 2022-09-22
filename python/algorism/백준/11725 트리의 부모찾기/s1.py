import sys

sys.stdin = open("input.txt")

t = int(input())

for tc in range(1, t + 1):
    n = int(input())

    ch1 = [0] * (n + 1)
    ch2 = [0] * (n + 1)

    # for i in range(n):
    #     par