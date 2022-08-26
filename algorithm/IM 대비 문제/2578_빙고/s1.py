import sys

sys.stdin = open('input')

visited = [[False] * 5 for _ in range(5)]
arr = [list(map(int, input().split())) for _ in range(5)]
data = [list(map(int, input().split())) for _ in range(5)]


for i in range(25):
    for j in range(25):
        if data[i][j] in arr:
            print()
print(arr)
print(data)
print(visited)