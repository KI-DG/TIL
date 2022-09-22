import sys
sys.stdin = open("input.txt")


def tree_make(start, end, n):
    if start == end:
        tree[n].append(data[start])
        return
    mid = (start + end) // 2
    tree[n].append(data[mid])
    tree_make(start, mid - 1, n + 1)
    tree_make(mid + 1, end, n + 1)



k = int(input())

data = list(map(int, input().split()))

ch1 = [0] * (k + 1)
ch2 = [0] * (k + 1)
tree = [[] for _ in range(k)]

tree_make(0, len(data)-1, 0)
for i in range(k):
    for j in tree[i]:
        print(j, end=' ')
    print()