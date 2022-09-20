import sys

dct = {'0001101': 0, '0011001': 1, '0010011': 2, '0111101': 3, '0100011': 4, '0110001': 5, '0101111': 6, '0111011': 7,
       '0110111': 8, '0001011': 9}
dct1 = {'0': '0000', '1': '0001', '2': '0010', '3': '0011', '4': '0100', '5': '0101', '6': '0110', '7': '0111',
        '8': '1000', '9': '1001', 'A': '1010', 'B': '1011', 'C': '1100', 'D': '1101', 'E': '1110', 'F': '1111'}

sys.stdin = open('input.txt')

t = int(input())

for tc in range(1, t + 1):
    n, m = map(int, input().split())

    row = [input() for i in range(n)]
    a = '0' * m

    num = ''
    for i in range(len(row)):
        if row[i] != a:
            num = row[i]
    e = m - 1
    while num[e] == '0':
        e -= 1

    answer = ''
    for j in range(e + 1):
        b = num[j]
        answer += dct1[b]
    v = len(answer) - 1
    while answer[v] == '0':
        v -= 1

    result = ''
    for x in range((v - 6) % 7, v + 1, 7):
        c = answer[x: x + 7]
        if c != '0000000':
            result += str(dct[c])

    cnt = 0
    for y in range(len(result)):
        if y % 2:
            cnt += int(result[y])
        else:
            cnt += 3 * int(result[y])

    count_a = 0
    for p in result:
        count_a += int(p)

    if cnt % 10 == 0:
        print(f'#{tc} {count_a}')
    else:
        print(f'#{tc} {0}')
