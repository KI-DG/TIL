import sys

sys.stdin = open('input.txt')

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
        max_index = L


pillar_list = [0] * (maxL + 1)
for l, h in pillar:
    pillar_list[l] = h
total = 0
max_height = 0
for j in range(max_index + 1):
    if pillar_list[j] > max_height:
        max_height = pillar_list[j]
