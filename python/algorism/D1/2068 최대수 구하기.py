t = int(input())
for tc in range(1, t + 1):
    data = list(map(int, input().split()))

    print(f'#{tc} {max(data)}')