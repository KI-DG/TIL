def preorder(n):
    if n:
        print(n, end=' ')
        preorder(ch1[n])
        preorder(ch2[n])


t = int(input())

for tc in range(1, t + 1):
    e = int(input())
    arr = list(map(int, input().split()))
    v = e + 1
    ch1 = [0] * (v + 1)
    ch2 = [0] * (v + 1)
    root = 1
    for i in range(e):
        p, c = arr[i * 2], arr[i * 2 + 1]
        if ch1[p] == 0:
            ch1[p] = c
        else:
            ch2[p] = c

    answer = preorder(root)

    print(f'#{tc} {answer}')