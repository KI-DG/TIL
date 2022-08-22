import sys

sys.stdin = open("input.txt")

t = int(input())

for tc in range(1, t + 1):
    test_case, n = input().split()  # test_case
    numbers = list(map(str, input().split()))  # 문자들이 들어있는 리스트

    data = {"ZRO": 0, "ONE": 1, "TWO": 2, "THR": 3, "FOR": 4, "FIV": 5, "SIX": 6, "SVN": 7, "EGT": 8, "NIN": 9}

    numbers.sort(key=lambda x: data[x])
    print(f'#{tc}')
    print(*numbers)
