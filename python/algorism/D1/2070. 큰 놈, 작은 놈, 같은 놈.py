t = int(input())

for tc in range(1, t + 1):
    x, y = map(int, input().split())

    if x < y:
        print(f'#{tc} <')
    elif x > y:
        print(f'#{tc} >')
    else:
        print(f'#{tc} =')