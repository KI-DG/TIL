import sys

sys.stdin = open("input.txt")

dct1 = {
        '0': '0000',
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
dct2 ={
    '001101': '0',
    '010011': '1',
    '111011': '2',
    '110001': '3',
    '100011': '4',
    '110111': '5',
    '001011': '6',
    '111101': '7',
    '011001': '8',
    '101111': '9',
}
t = int(input())

for tc in range(1, t + 1):
    # 16진수 2진수로 저장
    data = input()
    data_list = ''
    for i in data:
        data_list += dct1[i]
    # 우측 끝 부터 '1을 찾기
    e = len(data_list) - 1
    while data_list[e] == '0':
        e -= 1

    # 시작위치부터 6개씩 dct1 변환
    answer = []
    for i in range((e-5) % 6, e, 6):
        answer.append(dct2[data_list[i: i+6]])

    print(f'#{tc}', *answer)