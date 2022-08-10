import sys

sys.stdin = open("input")

t = int(input())

for tc in range(1, t+1):
    p, a, b = map(int, input().split())
    # p == 전체 쪽수

    start = 1
    end = p
    pa = 0
    while start <= end:
        center = int((start + end) / 2)
        pa += 1
        if center == a:
            break
        elif center < a:
            start = center
        elif center > a:
            end = center

    start = 1
    end = p
    pb = 0
    while start <= end:
        center = int((start + end) / 2)
        pb += 1
        if center == b:
            break
        elif center < b:
            start = center
        elif center > b:
            end = center

    if pa < pb:
        print(f"#{tc} A")
    elif pa > pb:
        print(f"#{tc} B")
    else:
        print(f"#{tc} 0")









