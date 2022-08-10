import sys

sys.stdin = open("input.txt")

t = int(input())
for tc in range(1, t+1):
    n = int(input())

    arr = [[0] * n for _ in range(n)]
    arr[0][0] = 1

    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]


    #
    # for i in range(n):
    #     for j in range(n):
    #
    print(arr)