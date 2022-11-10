import sys

sys.stdin = open("input.txt")

dct = {'0': '0000',
           '1': '0001',
           '2': '0010',
           '3': '0011',
           '4': '0100',
           '5': '0101',
           '6': '0110',
           '7': '0111',
           '8': '1000',
           '9': '1001',
           'A': '1010',
           'B': '1011',
           'C': '1100',
           'D': '1101',
           'E': '1110',
           'F': '1111',
           }
t = int(input())

for tc in range(1, t + 1):
    # 16진수를 2진수로 저장
    # 2진수를 다시 10진수로 저장
    answer = []
    n = 0
    data = input()

    for ch in data:
        answer += dct[ch]

    ans = []
    for i in range(len(answer)):
        n = int(answer[i]) + n * 2
        if (i % 7) == 6 or i == len(answer) - 1:
            ans.append(n)
            n = 0

    print(f'#{tc}', *ans)