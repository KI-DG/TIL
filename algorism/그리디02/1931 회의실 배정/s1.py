import sys

sys.stdin = open("input")


n = int(input())

arr = sorted([list(map(int, input().split())) for _ in range(n)], key=lambda x: (x[1], x[0]))

# 시작 조건
i = 0
j = 1
cnt = 1

while j < n:
    if arr[i][1] <= arr[j][0]:
        cnt += 1
        i = j
        j += 1
    else:
        j += 1

print(cnt)