import sys

sys.stdin = open('input.txt')


def baby_gin(arr):
    global answer
    sum_tri_run = 0

    for j in range(10):
        if arr[j] >= 3:
            sum_tri_run += 1
        if 0 < arr[j + 2] and 0 < arr[j + 1] and 0 < arr[j]:
            sum_tri_run += 1

    if sum_tri_run >= 1:
        return True


t = int(input())

for tc in range(1, t + 1):
    data = list(map(int, input().split()))
    player1 = [0] * 12
    player2 = [0] * 12
    answer = 0

    for idx, i in enumerate(data):
        if idx % 2:
            player2[i] += 1
            if idx >= 5:
                if baby_gin(player2):
                    answer = 2
                    break

        else:
            player1[i] += 1
            if idx >= 4:
                if baby_gin(player1):
                    answer = 1
                    break

    print(f'#{tc} {answer}')
