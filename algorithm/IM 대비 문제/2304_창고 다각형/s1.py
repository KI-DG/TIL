n = int(input())

maxH = 1
maxL = 0
pillar = []
for i in range(n):
    L, H = map(int, input().split())
    pillar.append([L, H])
    if maxL < L:
        maxL = L
    if maxH < H:
        maxH = H
        maxindex = L

    pillarlist = [0] * (maxL + 1)
    for l, h in pillar:
        pillarlist[l] = h

    total = 0
    temp = 0
    for i in range(maxindex + 1):
        if pillarlist[i] > temp:
            temp = pillarlist[i]