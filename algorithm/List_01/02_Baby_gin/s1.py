import sys

sys.stdin = open("input.txt")

T = int(input())

for tc in range(1, T + 1):
    N = input()  # 케이스를 받는 값
    card = [0] * 10  # 10개의 카드를 가지는 리스트
    i = run = tri = 0

    for j in N:
        card[int(j)] += 1
    # 숫자 카운트 증가
    while i < 10:

        if card[i] >= 3:
            card[i] -= 3
            tri += 1
            continue        # triplet을 구하는 경우

        if card[i] >= 1 and card[i + 1] >= 1 and card[i + 2] >= 1:
            card[i] -= 1
            card[i + 1] -= 1
            card[i + 2] -= 1
            run += 1
            continue            #run을 구하는 경우
        i += 1

    if run + tri == 2:
        print(f'#{tc} 1')
    else:
        print(f'#{tc} 0')
