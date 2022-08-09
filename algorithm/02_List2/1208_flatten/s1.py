import sys

sys.stdin = open("input")

for tc in range(1, 11):
    limit = int(input())
    data = list(map(int, input().split()))

    while limit:
        min_index = 0
        max_index = 0
        for i in range(1, 100):
            if data[i] < data[min_index]:
                min_index = i
            if data[i] > data[max_index]:
                max_index = i

        if (data[max_index] - data[min_index]) <= 1:
            break

        data[max_index] -= 1
        data[min_index] += 1
        limit -= 1

    min_index = 0
    max_index = 0
    for i in range(1, 100):
        if data[i] < data[min_index]:
            min_index = i
        if data[i] > data[max_index]:
            max_index = i

    print(f'#{tc} {data[max_index] - data[min_index]}')