import sys

sys.stdin = open("input")


def dfs(x):
    global ans

    if x == n:
        ans = max(ans, int("".join(map(str,lst))))
        return

    for i in range(L - 1):
        for j in range(i + 1, L):           # L개에서 2개 뽑는 조합
            lst[i], lst[j] = lst[j], lst[i]

            cst = ''.join(map(str, lst))
            if (n, cst) not in v:         # 방문 안 한 경우
                dfs(n+1)
                v.append((n, cst))
            lst[i], lst[j] = lst[j], lst[i]


t = int(input())

for tc in range(1, t + 1):
    st, n = input().split()
    N = int(n)
    lst = []
    for ch in st:
        lst.append(int(ch))
    v = []
    L = len(lst)
    ans = 0
    dfs(0)

    print(f'#{tc} {ans}')