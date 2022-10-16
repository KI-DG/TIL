import sys

sys.stdin = open('input.txt')
# 조합


def combinations(arr, start):
    global answer
    if len(arr) == length and sum(arr) == 100:
        answer += arr
        return

    for i in range(start, len(dwarf)):
        arr.append(dwarf[i])
        combinations(arr, i + 1)
        arr.pop()


dwarf = []
for _ in range(9):
    a = int(input())
    dwarf.append(a)

length = 7

answer = []
combinations([], 0)
answer.sort()

for j in range(7):
    print(answer[j])

# 틀렸습니다!
