N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]


s = 0
for i in range(N):
    for j in range(N):
        if i == j:
            s += arr[i][j]

s = 0
for i in range(N):
    s += arr[i][i]


s = 0
for i in range(N):
    s += arr[i][N-1-i]

# 대각선 양쪽합
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

s1 = s2 = 0
for i in range(N):
    for j in range(N):
        if i > j:
            s1 += arr[i][j]
        elif i < j:
            s2 += arr[i][j]

#
s1 = s2 = 0
for i in range(N):
    for j in range(i+1, N):
        s2 += arr[i][j]
        s1 += arr[j][i]