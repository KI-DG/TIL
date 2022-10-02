import sys

sys.stdin = open("input.txt")

n = int(input())
data = ['3', '6', '9']
ans = ''
for i in range(1, n + 1):
    cnt = 0
    a = str(i)
    for b in a:
        if b in data:
            cnt += 1

    if cnt == 0:
        ans += a
    else:
        for _ in range(cnt):
            ans += '-'
    ans += ' '

print(ans)