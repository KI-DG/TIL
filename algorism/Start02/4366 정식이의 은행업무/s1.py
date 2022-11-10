import sys

sys.stdin = open('input.txt')

t = int(input())

for tc in range(1, t + 1):
    # num_2 = list(input())
    # num_3 = list(input())
    #
    # result1 = []
    # result2 = []
    num1 = input()
    num2 = input()
    number1, number2 = [], []

    # 1. 2진수 모든 부분집합 생성
    for i1 in range(1, len(num1)):
        for j1 in range(2):
            bit1 = num1[:i1] + str(j1) + num1[i1 + 1:]
            if bit1 != num1:
                number1.append(bit1)

    # 2. 3진수 모든 부분집합 생성
    for i2 in range(len(num2)):
        for j2 in range(3):
            bit2 = num2[:i2] + str(j2) + num2[i2 + 1:]
            if bit2 != num2:
                number2.append(bit2)
    print(number1, number2)


    # for i in range(1, 1 << len(num_2)):
    #     for j in range(len(num_2)):
    #         if i & (1 << j):
    #             result1.append(num_2[j])
    #
    # for i in range(1, 1 << len(num_3)):
    #     for j in range(len(num_3)):
    #         if i & (1 << j):
    #             result2.append(num_3[j])
    #
    # for i in range(len(num_2)):
    #     for j in range(len(num_3)):
    #         ans1 = int(result1[i], 2)
    #         ans2 = int(result2[j], 3)
    #         print(ans1, ans2)

