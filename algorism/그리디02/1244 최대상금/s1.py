import sys

sys.stdin = open("input.txt")


def dfs(number):
    global ans
    if number == n:
        ans = max(ans, int("".join(map(str, lst))))
        return

    for i in range(a - 1):
        for j in range(i + 1, a):
            lst[i], lst[j] = lst[j], lst[i]

            cst = int("".join(map(str, lst)))
            if dct_v.get((number, cst), 1):
                dfs(number + 1)
                dct_v[(number, cst)] = 0

            lst[i], lst[j] = lst[j], lst[i]


t = int(input())
for test_case in range(1, t + 1):
    nums, change = input().split()
    n = int(change)
    lst = []
    for num in nums:
        lst.append(int(num))

    v = []
    dct_v = {}
    a = len(lst)
    ans = 0
    dfs(0)

    print(f'#{test_case} {ans}')