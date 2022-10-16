import sys

sys.stdin = open("input")

n = int(input())

arr = [[0] * 100 for _ in range(100)]

cnt = 0
for i in range(n):
    x, y = map(int, input().split())

    for j in range(y, y + 10):
        for k in range(x, x + 10):
            if arr[k][j] != 1:
                arr[k][j] = 1
                cnt += 1

print(cnt)