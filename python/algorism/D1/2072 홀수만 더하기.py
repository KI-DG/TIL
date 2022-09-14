t = int(input())

for tc in range(1, t + 1):
    data = list(map(int, input().split()))

    answer = 0
    for i in range(len(data)):
        if data[i] % 2:
            answer += data[i]

    print(f'#{tc} {answer}')