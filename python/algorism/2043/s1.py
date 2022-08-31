import sys

sys.stdin = open("input")


p, k = map(int, input().split())
print(p - k + 1)