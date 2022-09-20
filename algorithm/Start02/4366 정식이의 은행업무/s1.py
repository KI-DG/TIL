import sys

sys.stdin = open('input.txt')

t = int(input())

for tc in range(1, t + 1):
    num_2 = list(map(int, input()))
    num_3 = list(map(int, input()))

    for i in range(len(num_2)):
        result = ''
        if num_2[i] == 0:
            num_2[i] = 1
            result += str(num_2[i])
        elif num_2[i] == 1:
            num_2[i] = 0

    print(result)

