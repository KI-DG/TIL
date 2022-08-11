import sys

sys.stdin = open("input.txt")

t = int(input())

for tc in range(1, t+1):
    p, pa, pb = list(map(int, input().split()))
    # p == 전체쪽수 pa == a가 찾아야 될 쪽수 pb == b가 찾아야 될 쪽수

    # a가 찾는방법(횟수)
    start = 1
    end = p
    count_a = 0
    while start <= end:
        center = int((start + end)/2)
        count_a += 1
        if center < pa:
            start = center
        elif center > pa:
            end = center
        else:
            break

    # b가 찾는방법(횟수)
    start = 1
    end = p
    count_b = 0
    while start <= end:
        center = int((start + end)/2)
        count_b += 1
        if center < pb:
            start = center
        elif center > pb:
            end = center
        else:
            break

    if count_a < count_b:
        print(f"#{tc} A")
    elif count_a > count_b:
        print(f"#{tc} B")
    else:
        print(f"#{tc} 0")
