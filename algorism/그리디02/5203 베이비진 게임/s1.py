import sys

sys.stdin = open('input.txt')


def baby_gin(arr):
    sum_tri_run = 0
    for j in range(4):
        if arr[j] == arr[j + 1] == arr[j + 2]:
            sum_tri_run += 1
        if arr[j + 2] == arr[j + 1] + 1 == arr[j] + 2:
            sum_tri_run += 1

    return sum_tri_run


t = int(input())

for tc in range(1, t + 1):
    data = list(map(int, input().split()))
    play_1 = []
    play_2 = []

    for i in range(6):
        play_1.append(data[2 * i])
        play_2.append(data[2 * i + 1])

    p1 = sorted(play_1)
    p2 = sorted(play_2)

    if baby_gin(p1) == baby_gin(p2):
        print(f'#{tc} 0')
    elif baby_gin(p1) > baby_gin(p2):
        print(f'#{tc} 1')
    else:
        print(f'#{tc} 2')


# tc 중 7개만 맞음 중간에 먼저 이기는 경우를 생각해야된다.