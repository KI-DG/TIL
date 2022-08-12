import sys

sys.stdin = open("input.txt")

t = int(input())

for tc in range(1, t + 1):
    test_case, n = input().split()  # test_case
    numbers = list(map(str, input().split()))  # 문자들이 들어있는 리스트

    data = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]

    for idx1, number in enumerate(numbers):
        for idx2, val in enumerate(data):
            if number == val:
                numbers[idx1] = idx2

    for i1 in range(len(numbers)):
        for i2 in range(len(data)):
            if numbers[i1] == data[i2]:
                numbers[i1] = i2