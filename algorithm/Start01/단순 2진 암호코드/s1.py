import sys

sys.stdin = open("input.txt")

dct = {
    '0001101': 0,
    '0011001': 1,
    '0010011': 2,
    '0111101': 3,
    '0100011': 4,
    '0110001': 5,
    '0101111': 6,
    '0111011': 7,
    '0110111': 8,
    '0001011': 9,
}

t = int(input())

for tc in range(1, t + 1):

    n, m = map(int, input().split())
    # n은 세로의 크기 m은 가로크기

    row = [input() for _ in range(n)]
    arr = ''
    for i in range(n):
        if '1' in row[i]:
            arr = row[i]

    e = m - 1
    while arr[e] == '0':
        e -= 1

    answer = []
    for j in range((e - 6) % 7, e, 7):
        a = arr[j: j + 7]
        if a != '0000000':
            answer.append(dct[a])

    cnt = 0
    for x in range(len(answer)):
        if x % 2:
            cnt += answer[x]
        else:
            cnt += 3 * answer[x]

    if cnt % 10 == 0:
        print(f'#{tc} {sum(answer)}')
    else:
        print(f'#{tc} {0}')

    # 시작위치부터 6개씩 dct1 변환






















    # 숫자갯수로 저장 cnt 정렬 후 딕셔러니를 만든다