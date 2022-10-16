import sys

sys.stdin = open("input.txt")

n = int(input())

melon = [list(map(int, input().split())) for _ in range(6)]
melon_list1 = [0] * 5
melon_list2 = [1e9] * 5
result = []

for i, j in melon:
    melon_list1[i] += j
    if melon_list2[i] > j:
        melon_list2[i] = j

for i in range(1, 5):
    if melon_list2[i] != melon_list1[i]:
        result.append(melon_list2[i])

melon_list1.sort()
melon_big = melon_list1[1] * melon_list1[3]
melon_small = result[0] * result[1]

answer = n * (melon_big - melon_small)
print(answer)
