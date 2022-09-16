import sys

sys.stdin = open('input.txt')

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def room(r, c):
    cnt = 1
    while True:
        for k in range(4):  # 델타 검색을 하자
            ni = i + dx[k]
            nj = j + dy[k]
            if 0 <= ni < n and 0 <= nj < n and arr[ni][nj] - arr[i][j] == 1:  # 범위 안에 있다
                cnt += 1
                cnt_list.append(cnt)

    return cnt


t = int(input())

for tc in range(1, t + 1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]

    cnt_list = []

    for i in range(n):
        for j in range(n):
            room(arr[i][j])


