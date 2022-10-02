import sys

sys.stdin = open("input.txt")

t = int(input())

for tc in range(1, t + 1):
    data = list(map(int, input().split()))
    times, minutes = 0, 0

    for i in range(2):
        time, minute = data[i * 2], data[i * 2 + 1]
        times += time
        minutes += minute

    if minutes > 60:
        times += 1
        minutes -= 60

    if times > 12:
        times -= 12

    print(f'#{tc} {times} {minutes}')