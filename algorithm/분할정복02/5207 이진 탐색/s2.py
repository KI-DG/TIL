import sys

sys.stdin = open('input.txt')


def search(arr, value, position):
    global answer
    start, end = 0, len(arr) - 1

    while start <= end:
        center = (start + end) // 2   # left = start ~ center - 1 right = m + 1 ~ end
        if arr[center] == value:
            answer += 1
            return
        elif arr[center] > value:
            if position == -1:
                return
            end = center - 1
            position = -1
        else:
            if position == 1:
                return
            start = center + 1
            position = 1


t = int(input())

for tc in range(1, t + 1):
    n, m = map(int, input().split())
    data1_list = sorted(list(map(int, input().split())))
    data2_list = list(map(int, input().split()))
    answer = 0
    for y in range(m):
        search(data1_list, data2_list[y], 0)

    print(f'#{tc} {answer}')